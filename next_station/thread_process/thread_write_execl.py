# -*-coding:utf-8-*- 

"""
Author: Rage
Date: 19-4-26
"""
import xlwt
import queue
import threading
import time


StopEvent = object()


class ThreadPool:
    def __init__(self, max_num, max_tast_num=0):
        self.max_num = max_num  # 最大线程数
        if max_tast_num:    # 根据是否指定最大任务数来指定队列程度
            self.q = queue.Queue()  # 队列不限长度
        else:
            self.q = queue.Queue(max_tast_num)  # 根据用户指定长度创建队列

        self.generate_list = []  # 记录生成的线程
        self.free_list = []  # 记录空闲的线程
        self.terminal = False

    def run(self, target, args, callback=None):
        """运行该函数，调用线程池"""
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            # 没有空闲线程并且当前创建线程数量小于最大允许线程数量时允许创建线程
            self.creat_thread()  # 调用创建线程函数
        tast = (target, args, callback)  # 将任务打包成为元组放入队列
        self.q.put(tast)

    def creat_thread(self):
        """创建线程，并且运行，这时调用call函数，所有实现均在call函数内"""
        thread = threading.Thread(target=self.call)
        thread.start()

    def call(self):
        """线程调用该函数"""
        current_thread = threading.currentThread()  # 获取执行该函数的当前线程
        self.generate_list.append(current_thread)  # 将线程加入生成的线程列表

        tast = self.q.get()  # 从队列中取出一个任务包

        while tast != StopEvent:
            target, args, backcall = tast  # 将元组人物包，赋值给变量
            try:
                result = target(*args)  # 执行函数，并将返回值赋值给result
            except Exception as e:
                result = None

            if backcall:
                try:
                    backcall(result)  # 执行回调函数，并将result作为参数传给回调函数
                except Exception as e:
                    pass

            self.free_list.append(current_thread)  # 执行完毕，将当前线程对象加入空闲列表
            if self.terminal:  # 是否强制终止
                tast = StopEvent
            else:
                tast = self.q.get()  # 等待那任务，如果有任务直接循环执行，如果没有则等待，一旦run方法中放入任务则继续执行任务，无需再创建线程
            self.free_list.remove(current_thread)  # 拿到任务后，清除空闲线程
        else:
            self.generate_list.remove(current_thread)

    def close(self):
        """所有线程全部运行完毕后，停止线程
        call函数运行完毕后，所有的线程此时都在等待拿任务，此时，只要给队列里面添加StopEvent对象则线程就会结束"""
        generate_size = len(self.generate_list)
        while generate_size:
            self.q.put(StopEvent)
            generate_size -= 1

    def terminate(self):
        """不等待线程全部运行完毕任务，直接终止"""
        self.terminal = True  # 正在运行的线程运行完毕后会终止
        generate_size = len(self.generate_list)
        while generate_size:  # 终止已经在等待的那一部分线程
            self.q.put(StopEvent)
            generate_size -= 1


def func(li):
    for i in range(10000):
        li.append([i])


def world():
    wb = xlwt.Workbook()
    li = []
    pool = ThreadPool(5)
    for i in range(5):
        pool.run(target=func, args=(li,))
    pool.close()
    print(li)

    wb = xlwt.Workbook()
    ws = wb.add_sheet("sheet1")
    # ws.range("a1").value = li
    for i in range(len(li)):
        print(li[i])
        ws.write(i, 1, li[i])


if __name__ == '__main__':
    world()
