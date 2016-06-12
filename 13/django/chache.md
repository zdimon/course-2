##Cache

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }


    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'unix:/tmp/memcached.sock',
        }
    }


    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': [
                '172.19.26.240:11211',
                '172.19.26.242:11212',
                '172.19.26.244:11213',
            ]
        }
    }


    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'my_cache_table',
        }
    }




    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/var/tmp/django_cache',
            'TIMEOUT': 60,
            'OPTIONS': {
                'MAX_ENTRIES': 1000
            }
        }
    }

Chache views

    from django.views.decorators.cache import cache_page

    @cache_page(10)
    def home_page(request):


    @cache_page(10, cache="special_cache")
    CACHES = {
        'special_cache': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'my_cache_table',
        }
    }


###Specifying per-view cache in the URLconf

    from django.views.decorators.cache import cache_page

    urlpatterns = [
        url(r'^foo/([0-9]{1,2})/$', cache_page(60 * 15)(my_view)),
    ]



###Template fragment caching

    {% load cache %}
    {% cache 500 sidebar %}
        .. sidebar ..
    {% endcache %}

Sometimes you might want to cache multiple copies of a fragment 
depending on some dynamic data that appears inside the fragment.


    {% load cache %}
    {% cache 500 sidebar request.user.username %}
        .. sidebar for logged in user ..
    {% endcache %}


    {% load i18n %}
    {% load cache %}

    {% get_current_language as LANGUAGE_CODE %}

    {% cache 600 welcome LANGUAGE_CODE %}
        {% trans "Welcome to example.com" %}
    {% endcache %}


    {% cache 600 sidebar %} ... {% endcache %}
    {% cache my_timeout sidebar %} ... {% endcache %}


If you want to obtain the cache key used for a cached fragment, 
you can use make_template_fragment_key. fragment_name 


    >>> from django.core.cache import cache
    >>> from django.core.cache.utils import make_template_fragment_key
    # cache key for {% cache 500 sidebar username %}
    >>> key = make_template_fragment_key('sidebar', [username])
    >>> cache.delete(key) # invalidates cached template fragment

Accessing and basic using the cache.


    from django.core.cache import caches
    cache1 = caches['myalias']
    cache.set('my_key', 'hello, world!', 30)
    cache.get('my_key')
    cache.get('my_key', 'has expired')

If you want to get a key’s value or set a value 
if the key isn’t in the cache, there is the get_or_set() method. 

    cache.get_or_set('my_new_key', 'my new value', 100)

Deleting cache

    cache.delete('a')
    cache.clear()

###Caching model with cacheops

https://github.com/Suor/django-cacheops


    CACHEOPS_REDIS = {
        'host': 'localhost', # redis-server is on same machine
        'port': 6379,        # default redis port
        'db': 1,             # SELECT non-default redis database
                             # using separate redis db or redis instance
                             # is highly recommended

        'socket_timeout': 3,   # connection timeout in seconds, optional
        'password': '...',     # optional
        'unix_socket_path': '' # replaces host and port
    }

    # Alternatively the redis connection can be defined using a URL:
    CACHEOPS_REDIS = "redis://localhost:6379/1"
    # or
    CACHEOPS_REDIS = "unix://path/to/socket?db=1"
    # or with password (note a colon)
    CACHEOPS_REDIS = "redis://:password@localhost:6379/1"

    CACHEOPS = {
        # Automatically cache any User.objects.get() calls for 15 minutes
        # This includes request.user or post.author access,
        # where Post.author is a foreign key to auth.User
        'auth.user': {'ops': 'get', 'timeout': 60*15},

        # Automatically cache all gets and queryset fetches
        # to other django.contrib.auth models for an hour
        'auth.*': {'ops': ('fetch', 'get'), 'timeout': 60*60},

        # Cache gets, fetches, counts and exists to Permission
        # 'all' is just an alias for ('get', 'fetch', 'count', 'exists')
        'auth.permission': {'ops': 'all', 'timeout': 60*60},

        # Enable manual caching on all other models with default timeout of an hour
        # Use Post.objects.cache().get(...)
        #  or Tags.objects.filter(...).order_by(...).cache()
        # to cache particular ORM request.
        # Invalidation is still automatic
        '*.*': {'ops': (), 'timeout': 60*60},

        # And since ops is empty by default you can rewrite last line as:
        '*.*': {'timeout': 60*60},
    }
