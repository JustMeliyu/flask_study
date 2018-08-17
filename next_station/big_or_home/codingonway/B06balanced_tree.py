# encoding: utf-8

"""
输入一颗二叉树的根节点，判断该二叉树是不是平衡二叉树。
如果某二叉树中任意节点的左、右子树的深度相差不超过1，那么它就是一颗平衡二叉树。
"""


# 二叉树节点的定义如下
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


b_tree = TreeNode(3)
b_tree.right = TreeNode(2)
b_tree.left = TreeNode(2)

b_tree.left.left = TreeNode(4)
b_tree.left.left.left = TreeNode(5)


def is_balanced_tree(tree):
    left_lenght = 1
    right_lenght = 1
    if not tree:
        return True

    while tree.left is not None:
        left_lenght += 1
        tree.left = tree.left.left
    while tree.right is not None:
        right_lenght += 1
        tree.right = tree.right.right
    return abs(left_lenght - right_lenght) < 1


# print is_balanced_tree(b_tree)


class Solution(object):
    def __init__(self):
        pass

    def IsBalancedTree(self, pRoot):
        if not pRoot:
            return True
        return abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right)) <= 1
        # if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right)) > 1:
        #     return False
        # return self.IsBalancedTree(pRoot.left) and self.IsBalancedTree(pRoot.right)

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1


s = Solution()

print s.IsBalancedTree(b_tree)



