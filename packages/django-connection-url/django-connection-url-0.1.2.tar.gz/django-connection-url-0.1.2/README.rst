Django Connection URL
~~~~~~~~~~~~~~~~~~~~~

.. image:: https://secure.travis-ci.org/f0r4y312/django-connection-url.png?branch=master
   :target: http://travis-ci.org/f0r4y312/django-connection-url

This is a fork of Kenneth Reitz's `DJ-Database-URL <https://github.com/kennethreitz/dj-database-url>`_
extended to support cache URLs as well.

There are some significant changes to the original, most notably, ``.parse()``
has been dropped. You can pass URLs and environment variables to ``.config()``.
The passed value will be first checked if it is an environment variable, and if
not found it will be parsed as a URL. ``.config()`` will not use ``DATABASE_URL``
as default and therefore cannot be called without parameters.

The ``connection_url.config`` method returns a Django database/cache connection
dictionary, populated with all the data specified in your URL. Multiple
dictionary objects can be passed to ``.config()`` to set default values for
settings and options. Keyword arguments passed will override any default or
parsed values.

This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``DATABASE_URL`` environment variable to configure your Django application.

Supported Databases
-------------------

Support currently exists for PostgreSQL, PostGIS, MySQL, MySQL (GIS),
Oracle, Oracle (GIS), and SQLite.

Supported Caches
-------------------

Support currently exists for Redis, Memcached and local memory cache.

Installation
------------

Installation is simple::

    $ pip install django-connection-url

Usage
-----

Configure your database in ``settings.py`` from ``DATABASE_URL``::

    import connection_url

    DATABASES['default'] = connection_url.config('DATABASE_URL')

Provide an arbitrary Database URL::

    DATABASES['default'] = connection_url.config('postgres://...')

Set default values and override with keyword arguments::

    connection_url.config('mysql://username:password@hostname:5432/database?TIMEOUT=100', {
                          'ENGINE': 'django.contrib.gis.db.backends.postgis',
                          'CONN_MAX_AGE': 1000,
                          'OPTIONS': {'MAX_CONNECTIONS': 120},
                          }, ENGINE='django.db.backends.postgresql_psycopg2')
    #produces the following result
    {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database',
        'HOST': 'hostname',
        'PORT': 5432,
        'USER': 'username',
        'PASSWORD': 'password',
        'CONN_MAX_AGE': 1000,
        'OPTIONS': {'TIMEOUT': '100','MAX_CONNECTIONS': 120},
    }

The order of precedence for dict arguments, parsed values and keyword arg overrides is:
``Keyword arguments > Parsed values from connection URL > Defaults from passed dict objects.``

URL schema
----------

+-------------+----------------------------------------------------------+--------------------------------------------------+
| Engine      | Django Backend                                           | URL                                              |
+=============+==========================================================+==================================================+
| PostgreSQL  | ``django.db.backends.postgresql_psycopg2``               | ``postgres://USER:PASSWORD@HOST:PORT/NAME`` [1]_ |
+-------------+----------------------------------------------------------+--------------------------------------------------+
| PostGIS     | ``django.contrib.gis.db.backends.postgis``               | ``postgis://USER:PASSWORD@HOST:PORT/NAME``       |
+-------------+----------------------------------------------------------+--------------------------------------------------+
| MySQL       | ``django.db.backends.mysql``                             | ``mysql://USER:PASSWORD@HOST:PORT/NAME``         |
+-------------+----------------------------------------------------------+--------------------------------------------------+
| MySQL (GIS) | ``django.contrib.gis.db.backends.mysql``                 | ``mysqlgis://USER:PASSWORD@HOST:PORT/NAME``      |
+-------------+----------------------------------------------------------+--------------------------------------------------+
| SQLite      | ``django.db.backends.sqlite3``                           | ``sqlite:///PATH`` [2]_                          |
+-------------+----------------------------------------------------------+--------------------------------------------------+
| Oracle      | ``django.db.backends.oracle``                            | ``oracle://USER:PASSWORD@HOST:PORT/NAME`` [3]_   |
+-------------+----------------------------------------------------------+--------------------------------------------------+
| Oracle (GIS)| ``django.contrib.gis.db.backends.oracle``                | ``oraclegis://USER:PASSWORD@HOST:PORT/NAME``     |
+-------------+----------------------------------------------------------+--------------------------------------------------+
| Redis       | ``redis_cache.RedisCache``                               | ``redis://USER:PASSWORD@HOST:PORT`` [4]_         |
+-------------+----------------------------------------------------------+--------------------------------------------------+
| Memcached   | ``django.core.cache.backends.memcached.MemcachedCache``  | ``memcached://USER:PASSWORD@HOST:PORT``          |
+-------------+----------------------------------------------------------+--------------------------------------------------+
| Local memory| ``django.core.cache.backends.locmem.LocMemCache``        | ``locmem://HOST:PORT/PATH`` [5]_                 |
+-------------+----------------------------------------------------------+--------------------------------------------------+

.. [1] With PostgreSQL, you can also use unix domain socket paths with
       `percent encoding <http://www.postgresql.org/docs/9.2/interactive/libpq-connect.html#AEN38162>`_:
       ``postgres://%2Fvar%2Flib%2Fpostgresql/dbname``.
.. [2] SQLite connects to file based databases. The same URL format is used, omitting
       the hostname, and using the "file" portion as the filename of the database.
       This has the effect of four slashes being present for an absolute file path:
       ``sqlite:////full/path/to/your/database/file.sqlite``.
.. [3] Note that when connecting to Oracle the URL isn't in the form you may know
       from using other Oracle tools (like SQLPlus) i.e. user and password are separated
       by ``:`` not by ``/``. Also you can omit ``HOST`` and ``PORT``
       and provide a full DSN string or TNS name in ``NAME`` part.
.. [4] Requires ``django-redis-cache`` to be installed.
.. [5] For local memory cache, HOST:PORT/PATH is used as unique identifier for the cache.
       If none is given, a random UUID is used as identifier.
