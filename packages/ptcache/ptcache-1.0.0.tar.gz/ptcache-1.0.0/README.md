Simple cache based on the redis and cPickle for Python.

# Installation:

    pip install ptcache

# Usage:

## as a decorator for function

### use redis

```python
from ptcache import RedisCache, Cache

cache = Cache(RedisCache(password='***'))


@cache.cached(60*10)
def test(a, b, name='age'):
    return {"sum": a+b, "name": name}


@cache.uncache(test, kwarg_names=['name'])
def update_test(a, b, name="age"):
    return {"sum": a*b, "name": name}


# computed and stored on cache
test(1, 2)

# update and remove cache for function test
update_test(1, 2)

# remove cache manually
cache.remove_cache(test, 1, 2)
cache.remove_cache(test, 1, 2, name="age")

```

### use python object

```python
from ptcache import SimpleCache, Cache
import json

cache = Cache(SimpleCache(pickle=json))     # use json, default is cPickle


@cache.cached(60*10)
def test(a, b, name='age'):
    return {"sum": a+b, "name": name}


@cache.uncache(test, kwarg_names=['name'])
def update_test(a, b, name="age"):
    return {"sum": a*b, "name": name}


print(test(1, 2))
print(test(1, 2))
```

## as object

```python
from ptcache import RedisCache, SimpleCache

# use redis
cache = RedisCache(password='***')

cache.set('aaa', {'name':'fang', 'age':10, 'money': 12.03}, 60)
print(cache.exists('aaa'))
print(cache.get('aaa'))
print(cache.ttl('aaa'))

cache.delete('aaa')

print('*' * 10)

# use SimpleCache
cache = SimpleCache(timeout=20, threshold=5)
for x in range(6):
    cache.set(x, x)

print(cache.count())

for x in range(6):
    print(cache.exists(x))
    print(cache.ttl(x))
    print(cache.get(x))
    cache.delete(x)
    print('\n')

```