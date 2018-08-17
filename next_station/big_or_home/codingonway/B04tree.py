# encoding: utf-8
"""
输入两颗二叉树A和B，判断B是不是A的子结构，我们约定空树不是任意一个树的子结构
"""


# 二叉树节点的定义如下
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 要查找树A中是否存在和树B结构一样的子树，我们可以分成两步。
# 第一步，在树A中找到和树B的根节点的值一样的节点R。
# 第二步，判断树A中以R为根节点的子树是不是包含和树B一样的结构。
class Solution:
    def __init__(self):
        pass

    def HasSubtree(self, A, B):
        if not A or not B:
            return False
        return self.IsSubtree(A, B) or self.HasSubtree(A.left, B) or self.HasSubtree(A.right, B)

    def IsSubtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.IsSubtree(A.left, B.left) and self.IsSubtree(A.right, B.right)


tree_a = TreeNode(3)
tree_b = TreeNode(2)

tree_a.left = TreeNode(2)
tree_a.right = TreeNode(1)


is_tree = Solution()
print is_tree.HasSubtree(tree_a, tree_b)

