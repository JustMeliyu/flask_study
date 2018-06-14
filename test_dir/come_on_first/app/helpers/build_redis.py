# encoding: utf-8

import redis
from config import config, logger
from functools import wraps
from flask import g


r = redis.StrictRedis(
    host=config["REDIS_HOST"],
    port=config["REDIS_PORT"],
    password=config["REDIS_PASSWORD"],
    db=config["REDIS_DATABASE"],
    socket_timeout=3000
)


# 保存token到redis中
def check_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(g.token)
        user_info = r.hgetall(g.token)
        if user_info:
            return {"data": user_info}
        data = func(*args, **kwargs)
        if not data.get("ERROR"):
            logger.debug("set %s in '%s'" % (data.get("DATA").items(), g.token))
            print("data is %s " % data)
            r.hmset(g.token, data)
            logger.debug("set expire time %s with '%s' " % (config["APP_LOGIN_EXPIRE"], g.token))
            r.expire(g.token, config["APP_LOGIN_EXPIRE"])
            print r.hgetall(g.token)
        return data
    return wrapper


def is_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_info = r.hgetall(g.token)
        print(user_info)
        if not user_info:
            return {"ERROR": "TOKEN_EXPIRE"}
        else:
            current_user_id = user_info.get("DATA").get("telephone")
            g.current_user_id = current_user_id
        data = func(*args, **kwargs)
        return data
    return wrapper
