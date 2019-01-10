# encoding: utf-8

# 斐波那契数列，又称称黄金分割数列
a, b = 0, 1
while b < 100:
    a, b = b, a + b
    print "b is :", (b)
    print "a is :", (a)

a, b = 0, 1
a, b = b, a+b
print "a&b is :", a, b
# 这种赋值，先计算等值 右边 那么 b=1 a+b=1
# 再赋值给a和b，那么 a=1, b=1
a, b = 0, 1

a = b
# 此时 b=1, 那么a=1
b = a+b
# 那么 b=2
print "a&b is :", a, b

print "=========="
a = 12
b = 21


c = a
a = b
b = c
print "a&b is : ", a, b

e = 22
f = 33
e, f = f, e
print "e&f is : ", e, f
