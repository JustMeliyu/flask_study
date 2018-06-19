import redis

r = redis.StrictRedis(host="127.0.0.1", port=6379, password="", db=1, socket_timeout=3000)

a = {
    "da": "da",
    "qd": "qd"
}

b = [u"1", u"2", u"3"]
# r.hset("myhash", "a1", "aa")
# print type(r.hgetall("myhash"))
c = "1"
if c == b[0]:
    print(34333)
if c in b:
    print(111111111)
else:
    print(2222222)