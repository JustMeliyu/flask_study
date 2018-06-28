# encoding:utf-8
import time


class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month=month
        self.day=day

    @staticmethod
    def now():  # 用Date.now()的形式去产生实例,该实例用的是当前时间
        t = time.localtime()   # 获取结构化的时间格式
        return Date(t.tm_year,t.tm_mon,t.tm_mday)    # 新建实例并且返回

    @staticmethod
    def tomorrow():     # 用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t = time.localtime(time.time()+86400)
        return Date(t.tm_year,t.tm_mon,t.tm_mday)

    def __str__(self):
        return self.year

    def __repr__(self):
        return self.month

    def __getattr__(self, item):
        return item

a=Date('1987',11,27) #自己定义时间
b=Date.now() #采用当前时间
c=Date.tomorrow() #采用明天的时间
print(a)
print(a.year)
print(a.year, a.month, a.day)
print(b.year, b.month, b.day)
print(c.year, c.month, c.day)