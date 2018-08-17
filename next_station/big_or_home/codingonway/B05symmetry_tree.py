# encoding: utf-8
"""
实现一个函数，用来判断一颗二叉树是不是对称的。如果一颗二叉树和它的镜像一样，那么它是对称的
"""


# 二叉树节点的定义如下
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def symmetry_tree(tree):
    if not tree or (tree.left is None and tree.right is None):
        return True
    if tree.left is None or tree.right is None or tree.left.val != tree.right.val:
        return False
    return symmetry_tree(tree.left) and symmetry_tree(tree.right)


t_tree = TreeNode(3)
t_tree.right = TreeNode(2)
# t_tree.left = TreeNode(2)
# print t_tree.left
print symmetry_tree(t_tree)


class Solution(object):
    def __init__(self):
        pass

    def isSymmetrical(self, pRoot):
        return self.isSym(pRoot, pRoot)

    def isSym(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSym(pRoot1.left, pRoot2.right) and self.isSym(pRoot1.right, pRoot2.left)


s = Solution()

print s.isSymmetrical(t_tree)
