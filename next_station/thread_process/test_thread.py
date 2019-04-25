# -*-coding:utf-8-*- 

"""
Author: Rage
Date: 19-4-24
Refer: https://www.cnblogs.com/wongbingming/p/9028851.html
"""
import time
from threading import Thread
from datetime import datetime


def main(name="Python"):
    for i in range(2):
        print("name is {0}".format(name), datetime.now(), "\n")
        time.sleep(2)
        print("end is {0}".format(name), datetime.now(), "\n")


def run():
    thread1 = Thread(target=main)
    thread2 = Thread(target=main, args=['test'])
    # 启动子进程
    thread1.start()
    thread2.start()

    # 阻塞子进程, 待子线程结束后, 再忘下执行
    # thread1.join()

    # 判断子线程是否在执行状态, 在执行返回True, 否则返回False
    # thread1.is_alive()
    # thread1.isAlive()

    # 设置线程是否随主线程退出而退出, 默认为False
    # thread1.daemon = True

    # 设置线程名
    # thread1.name = ""


class MyThread(Thread):
    __doc__ = "类创建多线程"

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(2):
            print("Class, name is {0}".format(self.name), datetime.now(), "\n")
            time.sleep(2)
            print("Class, end is {0}".format(self.name), datetime.now(), "\n")


if __name__ == '__main__':
    run()

    thread3 = MyThread("test3")
    thread4 = MyThread("test4")

    thread3.start()
    thread4.start()
