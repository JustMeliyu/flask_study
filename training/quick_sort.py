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
        # mm = quick_sort3(left) + [mid] + quick_sort3(right)
        # print mm
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return origin_list


def quick_sort2(origin_list):
    for i in range(len(origin_list)):
        for j in range(len(origin_list) - 1, i - 1, -1):
            if origin_list[i] > origin_list[j]:
                origin_list[i], origin_list[j] = origin_list[j], origin_list[i]



if __name__ == "__main__":
    a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    a = quick_sort(a)
    # left:[2, 1]  mid:[3]  right:[40, 7, 34, 89, 432, 23, 89, 5, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  right:[40, 7, 34, 89, 432, 23, 89, 5, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[7, 34, 23, 5] mid:[40] right:[89, 432, 89, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[5] mid:[7] right:[34, 23] mid:[40] right:[89, 432, 89, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[5] mid:[7] left:[23] mid[34] right:[] mid:[40] right:[89, 432, 89, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[5] mid:[7] left:[23] mid[34] right:[] mid:[40] right:[89, 432, 89, 2222]


