# encoding: utf-8
# 函数执行异常重试装饰器
# 该decorator可以接收一个参数 'max_retry_count'
# 重试执行超过 max_retry_count 次的函数打印函数名字和异常类型
import traceback
from functools import wraps


def retry_func(max_retry_count):
    # 接收参数
    def _retry_func(func):
        @wraps(func)
        def try_to_do(*args, **kwargs):
            retry_count = 0
            e = None
            while retry_count < max_retry_count:
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    retry_count += 1
                    print "retry count {0}...".format(retry_count)
                    print traceback.format_exc(e)
                else:
                    return result
            print "ErrorType is {0}".format(repr(e))
            print "FunctionName is {0}".format(func.__name__)
            return None
        return try_to_do
    return _retry_func


def retry_func2(func):
    # 不带参数
    @wraps(func)
    def _retry_func2(*args, **kwargs):
        retry_count = 0
        e = None
        while retry_count < 5:
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                retry_count += 1
                print "retry count {0}...".format(retry_count)
                print traceback.format_exc(e)
            else:
                return result
        print "ErrorType is {0}".format(repr(e))
        print "FunctionName is {0}".format(func.__name__)
        return None
    return _retry_func2


@retry_func(3)
def func1(x):
    a = 6 / x
    print "result is {0}".format(a)
    return a


@retry_func2
def func2(x):
    a = 6 / x
    print "result is {0}".format(a)
    return a


if __name__ == "__main__":
    # re = func1(3)
    # print "result is {0}".format(re)
    re = func2(0)
    print "result is {0}".format(re)
