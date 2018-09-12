# encoding: utf-8
"""
二叉树的三种便利方法: 先序便利(根左右), 中序便利(左根右), 后序便利(左右根)
https://blog.csdn.net/wenkenza5368/article/details/79573333
"""

class TreeTrvaersal(object):
    # 二叉树的三种便利方法
    def __init__(self):
        self.li = list()

    # 递归实现三种遍历方式
    def pre_traversal(self, tree):
        # 二叉树的先序遍历
        # 先打印根节点, 再打印左节点, 最后打印右节点
        if tree is None:
            return
        self.li.append(tree.x)
        # print tree.x
        self.pre_traversal(tree.left)
        self.pre_traversal(tree.right)

    def in_traversal(self, tree):
        # 中序遍历
        # 先打印左节点, 再打印根节点, 最后打印右节点
        if tree is None:
            return
        self.in_traversal(tree.left)
        self.li.append(tree.x)
        # print tree.x
        self.in_traversal(tree.right)

    def post_traversal(self, tree):
        # 后序遍历
        # 先打印左节点, 再打印右节点, 最后打印根节点
        if tree is None:
            return
        self.post_traversal(tree.left)
        self.post_traversal(tree.right)
        self.li.append(tree.x)
        print tree.x

    # 迭代实现三种方式
    def preorder(self, tree):
        if not tree:
            return []
        stack = [tree]
        while stack:
            node = stack.pop()
            self.li.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return self.li

    def inorder(self, tree):
        stack = []
        node = tree
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.li.append(node.val)
            node = node.right
        return self.li

    def postorder(self, tree):
        stack = [tree]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            self.li.append(node.val)
        return self.li[::-1]

    @staticmethod
    def levelorder(tree):
        # 二叉树的层次遍历
        queue = [tree]
        res = []
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            res.append(node.val)
        return res
