# -*-coding:utf-8-*- 

"""
Author: Rage
Date: 19-4-26
"""

import xlwt
from threading import Thread
from next_station.common import is_thread_finish, get_func_time
from next_station.logger import logger


def write(ws, start_row):
    for j in range(256):
        ws.write(start_row, j, start_row * j)


@get_func_time
def run():
    wb = xlwt.Workbook()
    ws = wb.add_sheet("thread")
    thread_pool = []
    for i in range(20):
        t = Thread(target=write, args=(ws, i))
        thread_pool.append(t)
        t.start()

    is_thread_finish(thread_pool)
    wb.save("./test_thread.xls")


@get_func_time
def tradition():
    wb = xlwt.Workbook()
    ws = wb.add_sheet("tradition")
    for i in range(20):
        write(ws, i)
    wb.save("./test_tradition.xls")


@get_func_time
def coroutine():
    wb = xlwt.Workbook()
    ws = wb.add_sheet("tradition")
    for i in range(1000):
        gevent.join()


if __name__ == '__main__':
    run()
    tradition()

