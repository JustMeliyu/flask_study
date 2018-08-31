# encoding: utf-8
"""
冒泡排序原理即：从数组下标为0的位置开始，比较下标位置为0和1的数据，如果0号位置的大，则交换位置，
如果1号位置大，则什么也不做，然后右移一个位置，比较1号和2号的数据，和刚才的一样，如果1号的大，则交换位置，
以此类推直至最后一个位置结束，到此数组中最大的元素就被排到了最后，之后再根据之前的步骤开始排前面的数据，直至全部数据都排序完成。
"""
from functools import wraps
from datetime import datetime, timedelta

def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now1 = datetime.now()
        func(*args, **kwargs)
        now2 = datetime.now()
        print now2 - now1
    return wrapper

class Sort(object):
    def __init__(self):
        pass

    @classmethod
    def select_sort(cls, li):
        # 从第一个开始，依次比较从当前开始，列表之后的数据，若比当前小，则交换位置
        for i in range(len(li) - 1):
            for j in range(i + 1, len(li) - 1):
                if li[i] > li[j]:
                    li[i], li[j] = li[j], li[i]

    @classmethod
    def select_sort_simple(cls, li):
        for i in range(len(li)):
            for j in range(len(li) - i):
                if li[i] > li[i + j]:
                    li[i], li[i + j] = li[i + j], li[i]

    @classmethod
    def bubble_sort(cls, li):
        # 依次从第一个开始，比较后面的元素，大的放后面，直到最后一个，再从第一个开始
        for i in range(len(li) / 2 + len(li) % 2):
            for j in range(len(li) - 1 - i):
                if li[j] > li[j + 1]:
                    li[j], li[j + 1] = li[j + 1], li[j]


sort_list = [1, 5, 3, 8, 6, 7, 2, 3, 9]

# p = sorted(sort_list, key=lambda x: -x, reverse=True)
# print p

@run_time
def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


bubble_sort(sort_list)
print sort_list
sort_list = [1, 5, 3, 8, 6, 7, 2, 3, 9]
@run_time
def select_sort(li):
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li) - 1):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]


select_sort(sort_list)
print sort_list
