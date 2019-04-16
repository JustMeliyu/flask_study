# encoding: utf-8
"""
二叉树的三种便利方法:
先序便利(根左右),
    首先遍历根节点,
    然后遍历左子树,
    最后遍历右子树, 若子树为空则返回, 否则:
        访问根节点,
        先序遍历左子树,
        先序遍历右子树
中序便利(左根右),
    首先遍历左子树,
    然后遍历根节点,
    最后遍历右子树, 若子树为空则返回, 否则:
        中序遍历左子树,
        访问根节点,
        中序遍历右子树
后序便利(左右根)
https://blog.csdn.net/wenkenza5368/article/details/79573333
https://www.jianshu.com/p/bf73c8d50dc2
https://segmentfault.com/a/1190000008850005?utm_source=tag-newest
"""


class Tree(object):
    def __init__(self, x, left=None, right=None):
        self.x = x
        self.left = left
        self.right = right


class TreeTrvaersal(object):
    # 二叉树的三种便利方法
    def __init__(self, pre_view=None, in_view=None, post_view=None):
        self.view = list()
        self.pre_view = pre_view if pre_view is not None else []
        self.in_view = in_view if in_view is not None else []
        self.post_view = post_view if post_view is not None else []

    # 递归实现三种遍历方式
    def pre_traversal(self, tree):
        # 二叉树的先序遍历
        # 先打印根节点, 再打印左节点, 最后打印右节点.
        # 从二叉树的根结点出发, 当第一次到达结点时就输出结点数据, 按照先向左在向右的方向访问.
        if tree is None:
            return
        self.pre_view.append(tree.x)
        self.pre_traversal(tree.left)
        self.pre_traversal(tree.right)

    def in_traversal(self, tree):
        # 中序遍历
        # 先打印左节点, 再打印根节点, 最后打印右节点
        # 从二叉树的根结点出发, 当第二次到达结点时就输出结点数据, 按照先向左在向右的方向访问.
        if tree is None:
            return
        self.in_traversal(tree.left)
        self.in_view.append(tree.x)
        self.in_traversal(tree.right)

    def post_traversal(self, tree):
        # 后序遍历
        # 先打印左节点, 再打印右节点, 最后打印根节点
        # 从二叉树的根结点出发, 当第三次到达结点时就输出结点数据, 按照先向左在向右的方向访问.
        if tree is None:
            return
        self.post_traversal(tree.left)
        self.post_traversal(tree.right)
        self.post_view.append(tree.x)

    def get_post_view(self, pre_view, in_view):
        # 根据前序遍历及中序遍历计算后序遍历
        if len(pre_view) > 1:
            root_point = pre_view[0]
            left_tree_in_view = in_view[:in_view.index(root_point)]
            left_tree_pre_view = pre_view[1:len(left_tree_in_view) + 1]
            self.get_post_view(left_tree_pre_view, left_tree_in_view)

            right_tree_in_view = in_view[in_view.index(root_point) + 1:]
            right_tree_pre_view = pre_view[len(left_tree_in_view) + 1:]
            self.get_post_view(right_tree_pre_view, right_tree_in_view)
            # result = self.get_post_view(left_tree_pre_view, left_tree_in_view) + \
            #          self.get_post_view(right_tree_pre_view, right_tree_in_view) + [root_point]
            # return result
            self.post_view.append(root_point)
        elif len(pre_view) == 1:
            self.post_view.append(pre_view[0])
            # return [pre_view[0]]
        # else:
        #     return []

    # 迭代实现三种方式
    def preorder(self, tree):
        if not tree:
            return []
        stack = [tree]
        while stack:
            node = stack.pop(0)
            self.view.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return self.view

    def inorder(self, tree):
        stack = []
        node = tree
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.view.append(node.val)
            node = node.right
        return self.view

    def postorder(self, tree):
        stack = [tree]
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            self.view.append(node.val)
        return self.view[::-1]

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


def s_in_o(tree):
    if not tree:
        return []
    stack = []
    while stack:
        if stack[-1].right:
            stack.append(stack[-1].right)


fork_tree = Tree("a", Tree("b", Tree("f"), Tree("g")), Tree("c", Tree("d"), Tree("e")))
a = [1, 2, 4, 7, 3, 5, 8, 9, 6]
b = [4, 7, 2, 1, 8, 5, 9, 3, 6]

tree_TT = TreeTrvaersal()
# tree_TT.pre_traversal(fork_tree)
# print tree_TT.pre_view
print tree_TT.get_post_view(a, b)
# result [7, 4, 2, 8, 9, 5, 6, 3, 1]
# print tree_TT.post_view
