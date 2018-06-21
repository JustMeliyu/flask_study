# encoding: utf-8
from functools import wraps
from flask import request, make_response
from app.helpers.tool import *
from config import logger


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
        allow_headers = "Referer, Accept, Origin, User-Agent, x-requested-with"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun


# 校验相关参数是否存在或是否为空(去空格)
def check_params_exist(required=None):
    if not required:
        required = []

    def _check_params_exist(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for param in required:
                try:
                    val_param = request.values.get(param).strip()
                    if val_param == "":
                        return jsonify(get_result("PARAM_EMPTY", {}))
                except AttributeError:
                    try:
                        request.get_json(force=False, silent=True)[param]
                    except KeyError:
                        logger.debug("key %s is required" % param)
                        return jsonify(get_result("LACK_PARAM", {}))
                    except TypeError:
                        logger.debug("json is not dict")
                        return jsonify(get_result("LACK_PARAM", {}))
            val = func(*args, **kwargs)
            return val
        return wrapper
    return _check_params_exist

