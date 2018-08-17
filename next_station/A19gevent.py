# encoding: utf-8
import gevent


def test1():
    print(1, 2)
    gevent.sleep(2)  # 执行到这里的时候切换去函数test2
    print(3, 4)


def test2():
    print(5, 6)
    gevent.sleep(1)
    print(7, 8)


gevent.joinall(
    [gevent.spawn(test1), gevent.spawn(test2), gevent.spawn(test1())]
)  # 在函数test1等待的时候，协程去执行了函数test2