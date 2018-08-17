# encoding: utf-8
"""
交换字典的键和值
"""

d = {'A': 1, 'B': 2, 'C': 3}
# 字典推导式
d1 = {v: k for k, v in d.items()}
print d1

# 生成器表达式 + dict()
d2 = dict((v, k) for k, v in d.items())
print(d2)

# zip() + dict()
d3 = dict(zip(d.values(), d.keys()))
print(d3)

# 字典中的键必须是可哈希的不可变对象，值可以是任意对象。
# 因此交换字典的键和值可能会有两种意外情况。无法交换字典的键和值，原因是字典的值是不可哈希的。

# d = {'A': 1, 'B': [2], 'C': 3}
# d4 = {v: k for k, v in d.items()}

# 交换后字典元素数变少，原因是有重复值，字典的键具有唯一性。

d = {'A': 1, 'B': 1, 'C': 1}
d5 = {v: k for k, v in d.items()}
print(d5)
