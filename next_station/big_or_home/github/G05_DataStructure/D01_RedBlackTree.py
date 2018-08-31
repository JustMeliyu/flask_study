# encoding: utf-8
"""
https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/03.01.md
https://xieguanglei.github.io/blog/post/red-black-tree.html
各个节点: 每片树叶都长在一个结点上,这个结点就叫做这个叶子的父结点,
        这个叶子叫做你结点的子结点,没有子结点的结点叫叶子结点,没有父结点的结点叫根结点

由于红黑树本质上就是一棵二叉查找树,所以在了解红黑树之前,咱们先来看下二叉查找树.
二叉查找树(Binary Search Tree),也称有序二叉树(ordered binary tree),
排序二叉树(sorted binary tree),是指一棵空树或者具有下列性质的二叉树：
    1: 若任意结点的左子树不空,则左子树上所有结点的值均小于它的根结点的值;
    2: 若任意结点的右子树不空,则右子树上所有结点的值均大于它的根结点的值;
    3: 任意结点的左、右子树也分别为二叉查找树;
    4: 没有键值相等的结点(no duplicate nodes);

"""
