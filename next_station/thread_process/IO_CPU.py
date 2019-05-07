# -*-coding:utf-8-*- 

"""
Author: Rage
Date: 19-4-25
Refer: https://mings-blog.readthedocs.io/zh_CN/latest/c02/c02_01.html
https://mings-blog.readthedocs.io/zh_CN/latest/index.html
"""
import requests
import time
from threading import Thread
from next_station.common import get_func_time
from multiprocessing import Process
from next_station.logger import logger


# CPU计算密集型
def count(x=1, y=1):
    # 使程序完成150万计算
    c = 0
    while c < 500000:
        c += 1
        x += x
        y += y


# 磁盘读写IO密集型
def io_disk():
    with open("file.txt", "w") as f:
        for x in range(5000000):
            f.write("python-learning\n")


# 网络IO密集型
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
url = "https://www.baidu.com/"


def io_request():
    try:
        webPage = requests.get(url, headers=header)
        html = webPage.text
        return
    except Exception as e:
        return {"error": e}


# 【模拟】IO密集型
def io_simulation():
    time.sleep(2)


@get_func_time
def multi_thread(func, func_type=""):
    print("type is {0}".format(func_type))
    thread_list = []
    for i in range(10):
        t = Thread(target=func, args=())
        thread_list.append(t)
        t.start()
    e = len(thread_list)

    while True:
        for th in thread_list:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break


# # 多线程
# multi_thread(count, func_type="CPU计算密集型")
# multi_thread(io_disk, func_type="磁盘IO密集型")
# multi_thread(io_request, func_type="网络IO密集型")
# multi_thread(io_simulation, func_type="模拟IO密集型")


@get_func_time
def multi_process(func, fun_type=""):
    logger.info("multi_process type is {0}".format(fun_type))
    process_list = []
    for x in range(3):
        p = Process(target=func, args=())
        process_list.append(p)
        p.start()
    e = process_list.__len__()

    while True:
        for pr in process_list:
            if not pr.is_alive():
                e -= 1
        if e <= 0:
            break


if __name__ == '__main__':
    fun_list = [count, io_disk, io_request, io_simulation]
    for fun in fun_list:
        # multi_thread(fun)
        multi_process(fun)
