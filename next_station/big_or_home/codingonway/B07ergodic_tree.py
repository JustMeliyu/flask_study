# encoding: utf-8
"""
每次打印一个节点的时候，如果该节点有子节点，则把该节点的子节点放入到一个队列的末尾。
接下来到队列的头部取出最早进入队列的节点，重复前面的打印操作，直到队列中所有元素都被打印出来
"""
from collections import deque


# 二叉树节点的定义如下
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


b_tree = TreeNode(3)
b_tree.right = TreeNode(2)
b_tree.left = TreeNode(1)

b_tree.left.left = TreeNode(4)
b_tree.right.right = TreeNode(6)
b_tree.left.left.left = TreeNode(5)


def get_elements(tree):
    result = list()
    queue = deque()
    if tree:
        queue.append(tree)
        while queue:
            current = queue.popleft()
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return result


print get_elements(b_tree)
