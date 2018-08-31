# encoding:utf-8
"""
4.7 蚂蚁爬杆
一根27cm的细木杆，在3, 7, 11, 17, 23这几个位置分别有一个蚂蚁；
    1: 不能同时通过两只蚂蚁
    2: 开始时，蚂蚁是朝左还是朝右是任意的
    3: 它们只会朝前或调头，但不会后退
    4: 两只碰头后，会同时朝反方向调头走
    5: 蚂蚁每秒可以走1cm的距离
求所有蚂蚁都离开木杆的最短时间和最长时间

分析：
不能使用蛮力(brute force)
化繁为简，发现内在规律；

分析蚂蚁的运动状况，当两只蚂蚁碰头的时候会发送怎么样的情况
    虽然两只蚂蚁碰头后，都是调头忘回走，但是可以看做时两只蚂蚁相遇后的擦肩而过，继续忘前走；
    也就是说，每只蚂蚁的运动状态都是独立的，是否碰头并不重要
"""

li = [3, 7, 11, 17, 23]
length = 27
def ant_time():
    min_time = 0
    max_time = 0
    for i in li:
        min_time += min(length - i, i)
        max_time += max(length - i, i)
    return min_time, max_time


mintime, maxtime = ant_time()
print mintime, maxtime
