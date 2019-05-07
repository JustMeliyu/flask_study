# -*-coding:utf-8-*- 

"""
Author: Rage
Date: 19-4-26
setDeamon
"""
from next_station.common import get_func_time
from next_station.logger import logger
from threading import Thread, currentThread
import time


def action(arg):
    time.sleep(1)
    logger.info("sub Thread start! the thread name is {0}".format(currentThread().getName()))
    logger.info("the arg is {0}".format(arg))
    time.sleep(1)


@get_func_time
def run():
    thread_pool = list()
    for i in range(5):
        t = Thread(target=action, args=[i])
        # t.setDaemon(True)
        thread_pool.append(t)
        t.start()

    while True:
        for t in thread_pool:
            if not t.isAlive():
                logger.info("t{0} is finished".format(t.getName()))
                thread_pool.pop(thread_pool.index(t))
        if not thread_pool:
            break


if __name__ == '__main__':
    logger.info("main_thread start")
    run()
