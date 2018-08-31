# encoding: utf-8
"""
有一个无序，元素个数为2n的正整数数组，把这个数组分割为元素个数为n的两个数组，并使两个数组的和最接近
"""

li = [1, 3, 15, 8, 12, 45, 65, 47, 26, 39]


def solution(Olist):
    Slist = sorted(Olist)
    return Slist

class Solution(object):
    def __init__(self, Olist):
        self.Olist = sorted(Olist)
        self.Olist_one = [l for i, l in enumerate(self.Olist) if i % 2 == 0]
        self.Olist_two = [l for i, l in enumerate(self.Olist) if i % 2 != 0]
        print self.Olist_one
        print self.Olist_two

    def sum_sort(self):
        sum_one = sum(self.Olist_one)
        sum_two = sum(self.Olist_two)
        print "sum is {0} and {1}".format(sum_one, sum_two)
        complete = True
        for i, v1 in enumerate(self.Olist_one):
            for j, v2 in enumerate(self.Olist_two):
                if 0 < v2 - v1 < sum_two - sum_one:
                    self.Olist_two[j], self.Olist_one[i] = self.Olist_one[i], self.Olist_two[j]
                    complete = False
                    break
            break
        if not complete:
            self.sum_sort()
        return self.Olist_one, self.Olist_two


so = Solution(li)
one, two = so.sum_sort()
print one, two
