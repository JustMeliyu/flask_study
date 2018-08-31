# encoding: utf-8
"""
象棋中，将和帅分别在一个3*3的区域内，不能直接照面，
假设定义这个3*3的区域分别为1-9的坐标，求所有可能的组合集，且只能使用一个变量
1  2  3
4  5  6
7  8  9
"""
i = 81
while i != 0:
    i -= 1
    # if i / 9 % 3 == i % 9 % 3:
    #     continue
    if abs(i / 9 - i % 9) % 3 == 0:
        continue
    print "i is : {0} ;  A is : {1}, B is : {2}".format(i, i / 9 + 1, i % 9 + 1)
