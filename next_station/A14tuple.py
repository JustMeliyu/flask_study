# encoding: utf-8
from collections import Iterable

a = [1, 2, 3, 4, 5, 4, 2]
b = tuple(a)
print b
print type(b)
c = (1, 2, 3, 4, 5, 4, 2)
d = set(c)
print d
print type(d)
print set(a)

m = {1, 2, 4, 5, 3, 2, 4}
print m

n = set([1, 2, 3, 6, 2, 1])
print "n is : ", n

# 迭代器
for i, v in enumerate(a):
    print(i, v)
print enumerate(a)

print isinstance("abc", Iterable)

f = {"a": 1, "b": 2, "c": 3}
print f.items()
print f.keys()
for i in f.items():
    print i

# 列表生成器
mm = [m + n for m in "ABC" for n in "XYZ"]
print mm
print type(mm)
print [m * m for m in [2, 3, 4, 5, 6] if m % 2 == 0]

