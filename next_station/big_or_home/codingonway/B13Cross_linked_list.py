# encoding: utf-8
"""
交叉链表求交点
其实思想可以按照从尾开始比较两个链表，如果相交，则从尾开始必然一致，只要从尾开始比较，直至不一致的地方即为交叉点
"""
# 使用a,b两个list来模拟链表，可以看出交叉点是 7这个节点
a = [1, 4, 5, 7, 9, 1, 5]
b = [4, 5, 7, 9, 1, 5]

# 方法1: 正常循环
min_len = min(len(a), len(b))
for i in range(0, min_len):
    # 最后一个不相同
    if i == 0 and (a[-1] != b[-1]):
        print "No"
        break
    else:
        if a[-i - 1] != b[-i - 1]:
            print "交叉节点：", a[len(a) - i]
            print "a列表中索引为: ", len(a) - i
            print "b列表中索引为: ", len(b) - i
            break
        if i == min_len - 1:
            # 第一个相同
            print "交叉节点：", a[len(a) - i -1]
            print "a列表中索引为: ", len(a) - i - 1
            print "b列表中索引为: ", len(b) - i - 1
            break

# 方法2: 构造链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def node(l1, l2):
    length1, length2 = 0, 0
    # 求两个链表长度
    while l1.next:
        l1 = l1.next
        length1 += 1
    while l2.next:
        l2 = l2.next
        length2 += 1
    # 长的链表先走
    if length1 > length2:
        for _ in range(length1 - length2):
            l1 = l1.next
    else:
        for _ in range(length2 - length1):
            l2 = l2.next
    while l1 and l2:
        if l1.next == l2.next:
            return l1.next
        else:
            l1 = l1.next
            l2 = l2.next
