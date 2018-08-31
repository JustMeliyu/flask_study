# encoding: utf-8
"""
变位词: 一种把某个词或句子的字母的位置（顺序）加以改换所形成的新词，英文叫做anagram
譬如said(说，say的过去式)就有dais(讲台)这个变位词；
triangle（三角形）就有integral（构成整体所必要的）这个变位词；
Silent（不要吵）和Listen（听我说）也是。
"""

str_a = "Silent"
str_b = "Listen"

class Solution(object):
    def __init__(self):
        pass

    @classmethod
    def solution1(cls, first, second):
        first = first.upper()
        second = second.upper()

        for i, f in enumerate(first):
            if f not in second:
                print("不是变位词")
                return False
        for s in second:
            if s not in second:
                print("不是变位词")
                return False
        return True

    @classmethod
    def solution2(cls, first, second):
        alist = list(second)

        pos1 = 0
        stillOK = True

        while pos1 < len(first) and stillOK:
            pos2 = 0
            found = False
            while pos2 < len(alist) and not found:
                if first[pos1] == alist[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1

            if found:
                alist[pos2] = None
            else:
                stillOK = False

            pos1 = pos1 + 1

        return stillOK

    @classmethod
    def solution3(cls, s1, s2):
        alist1 = list(s1)
        alist2 = list(s2)

        alist1.sort()
        alist2.sort()

        pos = 0
        matches = True

        while pos < len(s1) and matches:
            if alist1[pos] == alist2[pos]:
                pos = pos + 1
            else:
                matches = False

        return matches

    @classmethod
    def solution4(cls, s1, s2):
        c1 = [0] * 26
        c2 = [0] * 26

        for i in range(len(s1)):
            pos = ord(s1[i]) - ord('a')
            c1[pos] = c1[pos] + 1

        for i in range(len(s2)):
            pos = ord(s2[i]) - ord('a')
            c2[pos] = c2[pos] + 1

        j = 0
        stillOK = True
        while j < 26 and stillOK:
            if c1[j] == c2[j]:
                j = j + 1
            else:
                stillOK = False

        return stillOK


print list(str_b)
print Solution.solution1(str_a, str_b)
