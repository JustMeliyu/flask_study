# encoding: utf-8
import gevent
from gevent import monkey
import urllib2
import time
from datetime import datetime
import requests
from next_station.common import max_conenct, get_func_time
monkey.patch_all()


@max_conenct
def get_body(count_i):
    print("start", count_i, datetime.now())
    requests.get("http://cn.bing.com")
    generate_data()
    print("end", count_i, datetime.now())
    return 1


@get_func_time
def generate_data():
    a = [i for i in xrange(10000000)]


@get_func_time
def test_xiecheng():
    tasks = [gevent.spawn(get_body, i) for i in range(3)]   # 启动协程
    gevent.joinall(tasks)   # 停止协程


@get_func_time
def test_common():
    get_body(0)
    get_body(1)
    get_body(2)


if __name__ == "__main__":
    print "start xiechen"
    test_xiecheng()
    time.sleep(3)
    print "start common"
    test_common()
