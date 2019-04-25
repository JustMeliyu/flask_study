# -*-coding:utf-8-*- 

"""
Author: Rage
Date: 19-4-25
"""
from threading import Thread, Event
import time
from datetime import datetime


class MyThread(Thread):
    __doc__ = "类创建多线程"

    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        for i in range(2):
            print("Class, name is {0}".format(self.name), datetime.now(), "\n")
            self.event.wait()
            print("Class, end is {0}".format(self.name), datetime.now(), "\n")


p_event = Event()

threads = [MyThread(str(i), p_event) for i in range(1, 5)]
