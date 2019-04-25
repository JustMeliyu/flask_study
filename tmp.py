# -*-coding:utf-8-*-
from threading import Thread


def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("函数注释", f.__annotations__)
    print("参数值打印", ham, eggs)
    print(type(ham), type(eggs))


f("rew")


def gen():
    for c in 'AB':
        yield c


print(list(gen()))


def gen_new():
    yield from 'AB'


print(list(gen_new()))

try:
    print(1)
except Exception as e:
    print(e)
    ...

a = 1
if not a:
    ...
else:
    print(111)

a = map(lambda x: x * 2, [1, 2, 3])
for i in a:
    print("===", i)


print("阿斯顿和")


def multi_thread(func, type=""):
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
