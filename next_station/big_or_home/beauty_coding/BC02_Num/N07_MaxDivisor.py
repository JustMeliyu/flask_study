# encoding:utf-8
"""
2.7章节  最大公约数
求两个正整数的最大公约数
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


# 解法1: 笨方法,但是当数字过大时,运行时间长,甚至超出内存限制
@run_time
def max_divisor1(num1, num2):
    max_d = 1
    for i in range(1, max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            max_d = i
    return max_d


# print max_divisor1(4567892, 12487244)


# 解法2: 辗转相除法
# f(x, y)表示两个数的最大公约数
# b=x%y; k=x/y; 则 x=k*y+b
# 如果一个数能同时整除x和y,则必能整除b和y;
# 而能够同时整除b和y的数也必能同时整除x和y，即它们的公约数时相同的,则最大公约数也是相同的
# 则有f(x, y)=f(y, x%y)(y>0)

def max_divisor2(num1, num2):
    # if num2 != 0 and num1 != 0:
    #     return max_divisor2(num2, num1 % num2)
    # return max(num1, num2)
    # return max_divisor2(num2, num1 % num2) if num2 != 0 and num1 != 0 else max(num1, num2)
    return (num2 != 0 and num1 != 0) and max_divisor2(num2, num1 % num2) or max(num1, num2)


now1 = datetime.now()
print max_divisor2(4567892, 12487244)
now2 = datetime.now()
print now2 - now1
# 解法3: 在解法2中,用到了取模运算.但对于大整数而言,取模运算(其中用到除法)是十分昂贵的开销,将成为整个算法的瓶颈
# 将解法2中的取模运算改为减法,即能够整除x和y,比能整除x-y和y

def max_divisor3(num1, num2):
    if num2 != 0 and num1 != 0:
        if num1 < num2:
            return max_divisor3(num2, num1)
        else:
            return max_divisor3(num2, num1 - num2)
    return max(num2, num1)


# print max_divisor3(4567892, 12487244)

