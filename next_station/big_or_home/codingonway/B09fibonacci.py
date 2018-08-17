# encoding: utf-8
"""
求斐波那契数列的第n项
求斐波那契数列的第n项，要求时间复杂度O(n)，空间复杂度O(1)。
在数学上，费波那契数列是以递归的方法来定义：
F（0）= 0
F（1）= 1
F（n）= F（n-1）+ F（n-2） （n >= 2）
特别指出：0不是第一项，而是第零项。
f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""

# 递归
# 递归的方法虽然简明清晰，但是开销太大，效率太低，会有大量的重复计算。
def fibonacci1(n):
    if n < 2:
        return n
    return fibonacci1(n - 1) + fibonacci1(n - 2)


print(fibonacci1(9))

# 递归优化版
# 优化版本的递归，把每次计算过的值都保存在字典中，避免大量重复计算。但却需要一个额外的辅助字典（空间复杂度O(n)）

kn = {0: 0, 1: 1}
def fibonacci2(n):
    if n not in kn.keys():
        kn[n] = fibonacci2(n - 1) + fibonacci2(n - 2)
    return kn[n]


print(fibonacci2(9))

# 循环
# 能用递归解决的问题在优化上的思路必然要考虑循环，而且用循环实现，效率高，开销小。
# 此方法时间复杂度O(n)，空间复杂度O(1)，是最佳的解决方案。
def fibonacci3(num):
    p, n = 0, 1
    for _ in range(num):
        p, n = n, p + n
    return p


print(fibonacci3(9))
