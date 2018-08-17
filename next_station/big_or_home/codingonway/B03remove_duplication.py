# encoding: utf-8
"""
如何去除列表中重复元素，如果要同时保证去重后元素顺序不变呢？
http://www.codingonway.com/python-remove-list-duplicate-items.html#more
"""
li = [1, 3, 1, 2, 4, 5, 6, 2]
li2 = list(set(li))
# 去除列表中重复元素，但改变来元素顺序
print li2
print {}.fromkeys(li)
print {}.fromkeys(li).keys()
print "===="
print li2.sort(key=li.index)

print sorted(set(li), key=li.index)


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item


li3 = list(dedupe(li))
print(li3)
