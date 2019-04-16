# encoding: utf-8
# generator函数, 在每次调用next()的时候执行, 遇到yield语句返回, 再次执行时从上次返回的yield语句处继续执行


def fib(max_index):
    n, a, b = 0, 0, 1
    while n < max_index:
        yield b
        a, b = b, a + b
        n = n + 1


# print fib(6)
# for i in fib(6):
#     print i


def MyGenerator():
    value = (yield 1)
    value = (yield value + 1)
    value = (yield value + 1)


gen = MyGenerator()
print gen.next()
print gen.send(2)
print gen.send(5)
# next
