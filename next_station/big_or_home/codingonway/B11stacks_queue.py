# encoding: utf-8
"""
栈是一种后进先出（LIFO）的数据结构，只能在一端（栈顶）插入和删除元素。
在Python中列表的append()和pop()方法分别对应的就是向栈顶插入和删除元素，因此Python中列表可以作为栈这种数据结构。

"""
from collections import deque

"""
队列是一种先进先出（FIFO）的数据结构，在一端（队尾）插入元素，在另一端（队首）删除元素。
列表的insert()和pop()方法，虽然可以实现队列的先进先出的特性，但是在列表头部插入和删除元素都不高效，因为需要移动列表后面的所有元素。
列表的特点是在尾部插入和删除元素时间复杂度O(1)，而在头部插入和删除元素时间复杂度O(n)。
为了实现队列，用collections.deque双端队列，其特点是可以在两端快速插入和删除元素，时间复杂度都为O(1)。
"""
print("队列===queue")
queue = deque([1, 2, 3, 4])
print(queue)
queue.append(5)
print(queue)
queue.append(6)
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

"""
问题描述：用两个栈实现一个队列。队列的声明如下，请实现它的两个方法enqueue和dequeue，分别完成在队列尾部插入节点和在队列头部删除节点的功能。
分析

用两个后进先出（LIFO）的栈，实现一个先进先出（FIFO）的队列。
队列尾部的插入元素操作可以用一个栈进行入栈操作代替，队列头部的删除操作需要用到第二个辅助栈，
当第二个辅助栈中没有元素时，将第一个栈中所有元素弹出然后压入到第二个辅助栈中，这样辅助栈出栈操作即是队列头部的删除操作，
如果第二个辅助栈中有元素，则直接出栈即可。
"""


class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.stack1)
q.dequeue()
print(q.stack2)
