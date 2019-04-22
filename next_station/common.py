from datetime import datetime
from functools import wraps
from next_station.logger import logger
from next_station.constant import APIEncoder
import json
import requests
import urllib2
import urllib
import traceback


def max_conenct(func):
    @wraps(func)
    def _max_connect(*args, **kwargs):
        _max = 5
        connect = 0
        e = None
        while connect < _max:
            try:
                func(*args, **kwargs)
            except Exception as e:
                print repr(e)
                connect += 1
                logger.error("connect is {0}".format(connect))
            else:
                break
        if connect == _max:
            print func.__name__
            logger.error("finally error is {0}".format(repr(e)))
    return _max_connect


def get_func_time(func):
    @wraps(func)
    def _get_func_time(*args, **kwargs):
        now1 = datetime.now()
        func(*args, **kwargs)
        now2 = datetime.now()
        logger.info("func is {0}, time spending is {1}".format(func.__name__, (now2 - now1).total_seconds()))
    return _get_func_time


def request_sys(req_url, request_data, method, reqheaders):
    logger.info("request_data is {0}".format(request_data))
    logger.info("headers is {0}".format(reqheaders))
    try:
        if 'GET' == method:
            request_data = urllib.urlencode(request_data).encode(encoding='utf-8')
            request = urllib2.Request(url="{0}?{1}".format(req_url, request_data), headers=reqheaders)
            res = urllib2.urlopen(request)
            result = res.read()
            logger.info("res content is {0}".format(result))
            return json.loads(result)
        elif 'POST' == method:
            reqheaders['Accept'] = 'application/json'
            if reqheaders.get('Content-Type') == 'application/json':
                request_data = json.dumps(request_data, cls=APIEncoder)
            result = requests.post(url=req_url, data=request_data, headers=reqheaders).content
            logger.info("res content is {0}".format(result))
            return json.loads(result)
        else:
            logger.info("method error, current method is {0}".format(method))
    except Exception as e:
        logger.error('request_order_sys access error:%s' % (traceback.format_exc(e),))
    return None
