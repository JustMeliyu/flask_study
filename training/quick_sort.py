# encoding: utf-8
__doc__ = """快速排序"""


def quick_sort(origin_list):
    print origin_list
    if len(origin_list) > 1:
        mid = origin_list[0]
        del origin_list[0]
        left = []
        right = []
        for i in origin_list:
            if i < mid:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return origin_list


def quick_sort2(origin_list):
    i = 0
    j = len(origin_list) - 1
    povit = origin_list[0]
    while i < j:
        while i < j and origin_list[j] >= povit:
            j -= 1
        if i < j:
            origin_list[i] = origin_list[j]
            i += 1

        while i < j and origin_list[i] < povit:
            i += 1


    if len(origin_list) > 1:
        start_index = 1
        for i in range(len(origin_list) - 1, -1, -1):
            if start_index == i + 1:
                # if origin_list[i] < origin_list[0]:
                origin_list[0], origin_list[i] = origin_list[i], origin_list[0]
                return quick_sort2(origin_list[:i]) + [origin_list[i]] + quick_sort2(origin_list[i + 1:])
                # else:
                #     origin_list[0], origin_list[i - 1] = origin_list[i - 1], origin_list[0]
                #     return quick_sort2(origin_list[:i - 1]) + [origin_list[i - 1]] + origin_list[i:]
            if origin_list[i] < origin_list[0]:
                for j in range(start_index, len(origin_list)):
                    if origin_list[j] > origin_list[0]:
                        origin_list[j], origin_list[i] = origin_list[i], origin_list[j]
                        start_index = j + 1
                        break
    else:
        return origin_list


if __name__ == "__main__":
    # a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    # a = [2, 89, 1, 432, 23, 89, 5, 2222]
    # print a[:3], [a[3]], a[4:]
    # a = [3, 1, 2, 34, 7, 89, 40, 432, 23, 89, 5, 2222]
    # a = [3, 1, 2, 34, 5, 7, 89, 40, 432, 23, 89, 5, 2222]
    a = [2, 1]
    # a = quick_sort(a)
    a = quick_sort2(a)
    print a
    # left:[2, 1]  mid:[3]  right:[40, 7, 34, 89, 432, 23, 89, 5, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  right:[40, 7, 34, 89, 432, 23, 89, 5, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[7, 34, 23, 5] mid:[40] right:[89, 432, 89, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[5] mid:[7] right:[34, 23] mid:[40] right:[89, 432, 89, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[5] mid:[7] left:[23] mid[34] right:[] mid:[40] right:[89, 432, 89, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[5] mid:[7] left:[23] mid[34] right:[] mid:[40] right:[89, 432, 89, 2222]

    # [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    # [1, 40, 7, 34, 2, 89, 3, 432, 23, 89, 5, 2222]    i = 0, j= 6
    # [1, 3, 7, 34, 2, 89, 40, 432, 23, 89, 5, 2222]    i = 1, j= 6
