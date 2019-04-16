from datetime import datetime
from functools import wraps


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
                print "connect is {0}".format(connect)
            else:
                break
        if connect == _max:
            print func.__name__
            print "finally error is {0}".format(repr(e))
    return _max_connect


def get_func_time(func):
    @wraps(func)
    def _get_func_time(*args, **kwargs):
        now1 = datetime.now()
        func(*args, **kwargs)
        now2 = datetime.now()
        print "func is {0}, time spending is {1}".format(func.__name__, (now2 - now1).total_seconds())
    return _get_func_time
