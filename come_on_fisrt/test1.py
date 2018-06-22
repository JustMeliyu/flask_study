# encoding: utf-8
import redis

r = redis.Redis()

# String 操作
print(u"String 操作:")
r.set('name', 'ly')
if r.get("asdasd"):
    print(22)
# r.mset(name1='lj', name2='ljj')
#
# print(r.get('name1'))
# r.append("name1", "append")
# print(r.get("name1"))
# print(r.incr("mount", amount=2))
# print(r.incr("mount"))
# print(r.incr("mount", amount=3))
# print(r.incr("mount", amount=4))
# r.delete("mount")
#
# print "======"
#
# # Hash 操作
# print u"Hash 操作:"
# r.hset("first_redis", "name", "ly")
# print r.hget("first_redis", "name")
#
# print r.hgetall("first_redis")
# dic = {
#     "school": "wuzhong",
#     "age": 18,
#     "sex": "man"
# }
# r.hmset("first_redis", dic)
# print "hgetall: %s" % r.hgetall("first_redis")
# print "hmget: %s" % r.hmget("first_redis", "age", "sex")
# print "hlen: %s" % r.hlen("first_redis")
# print "hkeys: %s" % r.hkeys("first_redis")
# print "hvals: %s" % r.hvals("first_redis")
# print "hexists: %s" % r.hexists("first_redis", "name")
# r.hdel("first_redis", "school")
# print "======"

# Set 操作
# print u"Set 操作:"
#
# r.sadd("first_redis_set", "ly")
# r.sadd("first_redis_set", "ly", "lj")
#
# print(r.smembers("first_redis_set"))
# print r.scard("first_redis_set")
#
# # 有序集合
# print u"有序集合"
# r.zadd("zset_name", "a", 6, "b", 2, "c", 5)
#
# print r.zcard("zset_name")
# print r.zcount("zset_name", 1, 5)


