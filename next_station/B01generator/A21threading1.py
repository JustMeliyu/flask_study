# encoding:utf-8
# 继承Thread式创建

import threading
import time


class MyThread(threading.Thread):

    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("running on number:%s" % self.num)
        time.sleep(3)


t1 = MyThread(56)
t2 = MyThread(78)

t1.start()
t2.start()
print("ending")
