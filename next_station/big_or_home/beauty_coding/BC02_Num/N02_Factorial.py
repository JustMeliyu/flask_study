# encoding: utf-8
"""
2.2章节
阶乘：
1: 给定一个整数N，那么N的阶乘  N! 尾末有多少个0。例如  N=10， N! = 3628800，末尾有两个0
2: 求 N! 的二进制表示中最低位1的位置
129的二进制为：10 000 001； 130的二进制为：10 000 010；
132的二进制为：10 000 100；
6! = 720， 二进制为  10 101 010 000
5! = 120， 二进制为      01 111 000
4! = 24， 二进制为       00 011 000
"""


# 问题1解法：计算所有元素中因子包含5的个数

def factorial_zero(num):
    count = 0
    for i in range(1, num + 1):
        while i % 5 == 0:
            i = i / 5
            count += 1
    return count


print factorial_zero(25)
# 问题2解法：能被2整除的因子数
def factorial_one(num):
    local = 1
    for i in range(1, num + 1):
        while i % 2 == 0:
            i = i / 2
            local += 1
    return local


print factorial_one(8)
