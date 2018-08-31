# encoding: utf-8
"""
2.1 章节
对于一个字节(8bit)的变量，求其二进制数中1的个数，要求算法的执行效率尽可能的高
"""

# 解法一： 对于二进制操作，除以一个2，原来的数字将会减少一个0

num = 19    # 00 010 011

def binary1(param):
    total = 0
    while param != 0:
        if param % 2 == 1:
            total += 1
        param = param / 2
    return total


total_num1 = binary1(num)
print "binary1 result : ", total_num1

# 解法二： 向右移位操作同样也可以达到相除的目的

def binary2(param):
    total = 0
    while param != 0:
        total += param & 0x01
        param >>= 1
    return total


total_num2 = binary2(num)
print total_num2
