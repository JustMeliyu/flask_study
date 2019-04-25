# -*-coding:utf-8-*-
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
except ValueError:
    ...
a = 1
if not a:
    ...
else:
    print(111)
