# Copyright 2015, 2016 Exponea s r.o. <info@exponea.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections import namedtuple
import inspect
try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse
from flask import current_app
import warnings
import redis
import redis.sentinel  # requires redis-py 2.9.0+
import redis_sentinel_url
import sys
from werkzeug.local import LocalProxy
from werkzeug.utils import import_string


if sys.version_info[0] == 2:  # pragma: no cover
    # Python 2.x
    _string_types = basestring

    def iteritems(d):
        return d.iteritems()
else:  # pragma: no cover
    # Python 3.x
    _string_types = str

    def iteritems(d):
        return d.items()

_EXTENSION_KEY = 'redissentinel'


class _ExtensionData(object):
    def __init__(self, client_class, sentinel=None, default_connection=None):
        self.client_class = client_class
        self.sentinel = sentinel
        self.default_connection = default_connection
        self.master_connections = {}
        self.slave_connections = {}

    def master_for(self, service_name, **kwargs):
        if self.sentinel is None:
            raise ValueError('Cannot get master {} using non-sentinel configuration'.format(service_name))
        if service_name not in self.master_connections:
            self.master_connections[service_name] = self.sentinel.master_for(service_name, redis_class=self.client_class,
                                                                             **kwargs)
        return self.master_connections[service_name]

    def slave_for(self, service_name, **kwargs):
        if self.sentinel is None:
            raise ValueError('Cannot get slave {} using non-sentinel configuration'.format(service_name))
        if service_name not in self.slave_connections:
            self.slave_connections[service_name] = self.sentinel.slave_for(service_name, redis_class=self.client_class,
                                                                           **kwargs)
        return self.slave_connections[service_name]


class _ExtensionProxy(LocalProxy):
    __slots__ = ('__sentinel',)

    def __init__(self, sentinel, local, name=None):
        object.__setattr__(self, '_ExtensionProxy__sentinel', sentinel)
        super(_ExtensionProxy, self).__init__(local, name=name)

    def _get_current_object(self):
        app = current_app._get_current_object()
        if _EXTENSION_KEY not in app.extensions or self.__sentinel.config_prefix not in app.extensions[_EXTENSION_KEY]:
            raise ValueError('RedisSentinel extension with config prefix {} was not initialized for application {}'.
                             format(self.__sentinel.config_prefix, app.import_name))
        ext_data = app.extensions[_EXTENSION_KEY][self.__sentinel.config_prefix]

        local = object.__getattribute__(self, '_LocalProxy__local')

        return local(ext_data)


class _PrefixedDict(object):
    def __init__(self, config, prefix):
        self.config = config
        self.prefix = prefix

    def _key(self, key):
        return '{}_{}'.format(self.prefix, key)

    def __getitem__(self, item):
        return self.config[self._key(item)]

    def __setitem__(self, item, value):
        self.config[self._key(item)] = value

    def __delitem__(self, item):
        del self.config[self._key(item)]

    def __contains__(self, item):
        return self._key(item) in self.config

    def get(self, item, default=None):
        return self.config.get(self._key(item), default)

    def pop(self, item, *args, **kwargs):
        return self.config.pop(self._key(item), *args, **kwargs)


class SentinelExtension(object):
    """Flask extension that supports connections to master using Redis Sentinel.

    Supported URL types:
      redis+sentinel://
      redis://
      rediss://
      unix://
    """
    def __init__(self, app=None, config_prefix=None, client_class=None, sentinel_class=None):
        self.config_prefix = None
        self.client_class = client_class
        self.sentinel_class = sentinel_class
        if app is not None:
            self.init_app(app, config_prefix=config_prefix)
        self.default_connection = _ExtensionProxy(self, lambda ext_data: ext_data.default_connection)
        self.sentinel = _ExtensionProxy(self, lambda ext_data: ext_data.sentinel)

    def init_app(self, app, config_prefix=None, client_class=None, sentinel_class=None):
        if _EXTENSION_KEY not in app.extensions:
            app.extensions[_EXTENSION_KEY] = {}

        extensions = app.extensions[_EXTENSION_KEY]

        if config_prefix is None:
            config_prefix = 'REDIS'

        if config_prefix in extensions:
            raise ValueError('Config prefix {} already registered'.format(config_prefix))

        self.config_prefix = config_prefix

        config = _PrefixedDict(app.config, config_prefix)
        url = config.get('URL')

        client_class = self._resolve_class(config, 'CLASS', client_class, 'client_class',
                                           default=redis.StrictRedis)
        sentinel_class = self._resolve_class(config, 'SENTINEL_CLASS', sentinel_class, 'sentinel_class',
                                             default=redis.sentinel.Sentinel)

        data = _ExtensionData(client_class)

        if url:
            connection_options = self._config_from_variables(config, client_class)
            sentinel_options = self._config_from_variables(_PrefixedDict(config, 'SENTINEL'), client_class)

            connection_options.pop('host', None)
            connection_options.pop('port', None)
            connection_options.pop('db', None)

            result = redis_sentinel_url.connect(url, sentinel_class=sentinel_class,
                                                sentinel_options=sentinel_options,
                                                client_class=client_class,
                                                client_options=connection_options)
            data.sentinel, data.default_connection = result
        else:
            # Stay compatible with Flask-And-Redis for a while
            warnings.warn('Setting redis connection via separate variables is deprecated. Please use REDIS_URL.',
                          DeprecationWarning)
            kwargs = self._config_from_variables(config, client_class)
            data.default_connection = client_class(**kwargs)

        extensions[config_prefix] = data

    def _resolve_class(self, config, config_key, the_class, attr, default):
        if the_class is not None:
            pass
        elif getattr(self, attr) is not None:
            the_class = getattr(self, attr)
        else:
            the_class = config.get(config_key, default)
            if isinstance(the_class, _string_types):
                the_class = import_string(the_class)
        return the_class

    @staticmethod
    def _config_from_variables(config, client_class):
        host = config.get('HOST')
        if host and (host.startswith('file://') or host.startswith('/')):
            del config['HOST']
            config['UNIX_SOCKET_PATH'] = host

        args = inspect.getargspec(client_class.__init__).args
        args.remove('self')

        def get_config(suffix):
            value = config[suffix]
            if suffix == 'PORT':
                return int(value)
            return value

        return {arg: get_config(arg.upper()) for arg in args if arg.upper() in config}

    def master_for(self, service_name, **kwargs):
        return _ExtensionProxy(self, lambda ext_data: ext_data.master_for(service_name, **kwargs))

    def slave_for(self, service_name, **kwargs):
        return _ExtensionProxy(self, lambda ext_data: ext_data.slave_for(service_name, **kwargs))