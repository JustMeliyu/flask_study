# encoding: utf-8
# 斐波那契数列，又称称黄金分割数列
a, b = 1, 1
m = [a, b]
while b < 100:
    a, b = b, a + b
    print "b is :", (b)
    print "a is :", (a)
    m.append(b)
print m


def fib(max_len):
    n, x, y = 0, 0, 1
    while n < max_len:
        print y
        x, y = y, x + y
        n += 1


s = fib(6)
print s
print type(s)
print s.next()





