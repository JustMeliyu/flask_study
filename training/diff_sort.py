# encoding: utf-8
__doc__ = """不同排序方法"""
TOTAL_COUNT = 1


def select_sort(origin_list):
    a = [3, 40, 50, 1, 40, 20, 80]
    # 选择排序
    k = 0
    for i in range(len(origin_list) - 1):
        _min = i
        for j in range(i + 1, len(origin_list)):
            if origin_list[_min] > origin_list[j]:
                _min = j
            k += 1
        print _min
        origin_list[i], origin_list[_min] = origin_list[_min], origin_list[i]
        print origin_list
    return origin_list


def bubble_sort(origin_list):
    # 冒泡排序
    k = 0
    for i in range(len(origin_list) - 1):
        for j in range(len(origin_list) - i - 1):
            if origin_list[j + 1] < origin_list[j]:
                origin_list[j + 1], origin_list[j] = origin_list[j], origin_list[j + 1]
                # print origin_list
            k += 1
        # print "round {0}".format(i - 1)
    print "total count is {0}".format(k)
    return origin_list


def afunc(z):
    global TOTAL_COUNT
    TOTAL_COUNT += 1
    if z <= 1:
        return 1
    else:
        return afunc(z - 1) + afunc(z - 2)


def quick_sort(origin_list):
    for i in range(len(origin_list) - 1):
        for j in range(len(origin_list) - 1, i - 1, -1):
            if origin_list[i] > origin_list[j]:
                origin_list[i], origin_list[j] = origin_list[j], origin_list[i]
                print origin_list
            if i == j:
                break
    return origin_list


def quick_sort2(data):
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口
        mid = data[len(data) // 2]  # 选取基准值，也可以选取第一个或最后一个元素
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


def quick_sort3(origin_sort):
    if len(origin_sort) > 1:
        mid = origin_sort[0]
        del origin_sort[0]
        left = []
        right = []
        for i in origin_sort:
            if i < mid:
                left.append(i)
            else:
                right.append(i)
        # mm = quick_sort3(left) + [mid] + quick_sort3(right)
        # print mm
        return quick_sort3(left) + [mid] + quick_sort3(right)
    else:
        return origin_sort


if __name__ == "__main__":
    # a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    # a = [3, 40, 50, 1, 40, 20, 80]
    # b = select_sort(a)
    # print b
    # print "======"
    # c = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    # d = bubble_sort(c)
    # print d
    # n = 5
    # s = (n - 1) * n + (n - 1) * (n - 1) + (n - 1) * (n - 2)
    # k = (n - 1) * (n * n - )
    # a = afunc(10)
    # print "a is {0}".format(a)
    # print TOTAL_COUNT
    a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    b = quick_sort3(a)
    print b
