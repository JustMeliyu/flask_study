# encoding: utf-8
import math
from datetime import datetime, timedelta
from collections import Iterable
# 按列表输出
now1 = datetime.now()
li = [line.strip('\n') for line in open("e.txt", "r")]
n = 0
for num in li:
    if n < 10:
        print num, len(num)
        n += 1
    else:
        break

# 按生成器输出
now2 = datetime.now()
gen = (line.strip('\n') for line in open("e.txt", "r"))
n = 0
for num in gen:
    if n < 10:
        print num
        n += 1
    else:
        break
now3 = datetime.now()
timedelta1 = (now2 - now1).microseconds
timedelta2 = (now3 - now2).microseconds
print "==========="
print "按列表输出间隔: {0} 微秒".format(timedelta1)
print "按生成器输出间隔: {0} 微秒".format(timedelta2)
