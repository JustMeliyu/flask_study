import redis
REDIS_DB = 1
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = ''
REDIS_URL = 'redis://:%s@%s:%s/%s' % (REDIS_PASSWORD, REDIS_HOST, REDIS_PORT, REDIS_DB)
url = 'redis://:@127.0.0.1:6379/1'
# print url
# print REDIS_URL
r = redis.from_url(url)

a = {
    "a": 1,
    "b": 2
}
b = [1, 2, 3]
# r.set("te", "a", a)

# r.set("te2", b)
# r.set("te2", b)
# r.set("te2", b)
