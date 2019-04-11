# encoding: utf-8
"""

二叉树的左旋和右旋
"""
from T02_TreeTrvaersal import TreeTrvaersal


class Tree(object):
    def __init__(self, x, left=None, right=None):
        self.x = x
        self.left = left
        self.right = right


# 左旋
# fork_tree = Tree("a", Tree("b"), Tree("c", Tree("d"), Tree("e")))
# 右旋
fork_tree = Tree("a", Tree("b", Tree("d"), Tree("e")), Tree("c"))
# fork_tree = Tree("a", Tree("b", Tree("f"), Tree("g")), Tree("c", Tree("d"), Tree("e")))


tt = TreeTrvaersal()
tt.pre_traversal(fork_tree)
# tt.in_traversal(fork_tree)
# tt.post_traversal(fork_tree)
print tt.li


class TreeRotato(object):
    def __init__(self):
        self.root = None

    @staticmethod
    def left_rotato(tree):
        # 左旋, 自己变成右孩子的左孩子
        tmp = tree.right.left           # tmp.x = d
        tree.right.left = Tree(tree.x)
        tree.right.left.left = tree.left
        tree.right.left.right = tmp
        return tree.right

    @staticmethod
    def right_rotato(tree):
        # 右旋, 自己变成左孩子的右孩子
        tmp = tree.left.right
        tree.left.right = Tree(tree.x)
        tree.left.right.left = tmp
        tree.left.right.right = tree.right
        return tree.left


# 先序遍历, 左旋 ['a', 'b', 'c', 'd', 'e']  =>  ['c', 'a', 'b', 'd', 'e']
# fork_tree = left_rotato(fork_tree)
tt.li = []
# tt.pre_traversal(fork_tree)
# print tt.li

# 先序遍历, 右旋 ['a', 'b', 'd', 'e', 'c']  =>  ['b', 'd', 'a', 'e', 'c']
tt.li = []
fork_tree = TreeRotato.right_rotato(fork_tree)
tt.pre_traversal(fork_tree)
print tt.li
