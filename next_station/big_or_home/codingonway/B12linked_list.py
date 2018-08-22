# encoding: utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def __init__(self):
#         pass
#
#     def exchange_list(self, listnode):
#         if listnode is not None:
#             listnode.val, listnode.next.val = listnode.next.val, listnode.val
#             # print listnode.val
#             return self.exchange_list(listnode.next.next)
class Solution(object):
    # @param a ListNode
    # @return a ListNode
    def __init__(self):
        pass

    def swapPairs(self, prev):
        if prev is not None and prev.next is not None:
            curr = prev.next
            prev.next = self.swapPairs(curr.next)
            curr.next = prev
            return curr
        return prev


li = ListNode(1)
li.next = ListNode(2)
# print li.next
# print li.next.val
li.next.next = ListNode(3)
# print li.next.next.val
li.next.next.next = ListNode(4)

so = Solution()
# so.exchange_list(li)
m = so.swapPairs(li)
print(m)
print(m.val)
print(m.next.val)
print(m.next.next.val)
print(m.next.next.next.val)
print li.val
print li.next.val
print li.next.next.val
# print li.next.next.next.val
