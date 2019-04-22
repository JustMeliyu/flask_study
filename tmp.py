# -*-coding:utf-8-*-
a = ["a", "b", "c"]
b = [1, 2, 3]
c = dict(map(lambda x, y: (x, y), a, b))
print(c)
