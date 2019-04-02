# encoding=utf-8
import gc
import time

__author__ = 'kevinlu1010@qq.com'


class ClassA(object):
    def __init__(self):
        print 'object born,id:%s' % str(hex(id(self)))

    def __del__(self):
        print 'object del,id:%s' % str(hex(id(self)))


def f1():
    i = 0
    a = list()
    while i < 10000000:
        a.append(ClassA())
        i += 1


def f3():
    c1 = ClassA()
    c2 = ClassA()
    # c1.t = c2
    # c2.t = c1
    # del c1
    # del c2
    print gc.garbage
    gc.collect()  # 显式执行垃圾回收
    print gc.garbage
    time.sleep(10)


def f4():
    try:
        a = 1 / 0
    except Exception as e:
        print repr(e)


if __name__ == '__main__':
    f4()
#     gc.enable()
#     gc.set_threshold(100, 5, 5)
#     gc.set_debug(gc.DEBUG_LEAK)  # 设置gc模块的日志
#     f3()
#
# # if __name__ == "__main__":
# #     f1()
