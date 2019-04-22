# encoding: utf-8
__doc__ = """快速排序"""


def quick_sort(origin_list):
    print(origin_list)
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


def quick_sort2(myList):
    # a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    # 判断low是否小于high,如果为false,直接返回
    if len(myList) > 0:
        i = 1
        j = len(myList) - 1
        # 设置基准数
        base = myList[0]

        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            # 同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1

            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            if i < j:
                myList[i], myList[j] = myList[j], myList[i]

            # 同样的方式比较前半区
            # while (i < j) and (myList[i] <= base):
            #     i = i + 1
            # myList[j] = myList[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        # myList[i] = base

        # 递归前后半区
        return quick_sort4(myList[:i]) + [myList[i]] + quick_sort4(myList[i + 1:])
    return myList


def quick_sort3(myList, start, end):
    # 判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = myList[i]

        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            # 同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        # 递归前后半区
        quick_sort3(myList, start, i - 1)
        quick_sort3(myList, j + 1, end)
    return myList


def quick_sort4(myList):
    # 判断low是否小于high,如果为false,直接返回
    if len(myList) > 0:
        i = 0
        j = len(myList) - 1
        # 设置基准数
        base = myList[i]

        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            # 同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        # 递归前后半区
        return quick_sort4(myList[:i]) + [myList[i]] + quick_sort4(myList[i + 1:])
    return myList


if __name__ == "__main__":
    a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    # a = [2, 89, 1, 432, 23, 89, 5, 2222]
    # print a[:3], [a[3]], a[4:]
    # a = [3, 1, 2, 34, 7, 89, 40, 432, 23, 89, 5, 2222]
    # a = [5, 1, 2, 34, 5, 7, 89, 40, 432, 23, 89, 3, 2222]
    # a = [2, 1]
    # a = quick_sort(a)
    # a = quick_sort2(a)
    a = quick_sort4(a)
    print(a)
    # left:[2, 1]  mid:[3]  right:[40, 7, 34, 89, 432, 23, 89, 5, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  right:[40, 7, 34, 89, 432, 23, 89, 5, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[7, 34, 23, 5] mid:[40] right:[89, 432, 89, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[5] mid:[7] right:[34, 23] mid:[40] right:[89, 432, 89, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[5] mid:[7] left:[23] mid[34] right:[] mid:[40] right:[89, 432, 89, 2222]
    # left:[1] mid:[2] right:[]  mid:[3]  left[5] mid:[7] left:[23] mid[34] right:[] mid:[40] right:[89, 432, 89, 2222]

    # [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    # [1, 40, 7, 34, 2, 89, 3, 432, 23, 89, 5, 2222]    i = 0, j= 6
    # [1, 3, 7, 34, 2, 89, 40, 432, 23, 89, 5, 2222]    i = 1, j= 6
