# encoding: utf-8
"""
我们有一个字典列表，想根据一个或多个字典中的值来对列表排序。
例如，有如下字典列表，根据字典中的x，由大到小排序这个列表：
http://www.codingonway.com/python-sorted-dict-list-by-common-keys.html#more
"""
from operator import itemgetter
li = [{'x': 7, 'y': 1}, {'x': 7, 'y': 2}, {'x': 7, 'y': 8}, {'x': 6, 'y': 3},
      {'x': 3, 'y': 7}, {'x': 3, 'y': 5}, {'x': 3, 'y': 2}]

nn = [1, 3, 8, 2, 5, 3, 8, 9]
dd = {"x": 7, "y": 1, "z": 4}
# for di in li:
sorted(nn)

print sorted([x.get('x') for x in li])
print sorted(li, key=lambda di: (di.get('x'), di.get('y')))
print sorted(li, key=itemgetter('x', 'y'))
print sorted(li, cmp=lambda x, y: cmp(x.get('x'), y.get('x')))
print "sort dict : ", sorted(dd.items(), key=lambda x: x[1])
print callable(itemgetter('x', 'y'))

# 同样适用于min()，max()等函数

print min(li, key=lambda di: (di.get('x'), di.get('y')))
print max(li, key=lambda di: (di.get('x'), di.get('y')))

