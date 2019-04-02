# encoding:utf-8
from random import randint
# check the (i,j) is in the matrix index


def generate_map(row, col):
    return [[randint(0, 100) for j in range(col)] for i in range(row)]


def isInside(row, col, i, j):
    return (i in range(row)) and (j in range(col))


# get the max step from the current point
def currentMaxStep(data, row, col, i, j):
    max_step = 0
    directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for (dx, dy) in directs:
        x, y = i + dx, j + dy
        if isInside(row, col, x, y) and data[x][y] < data[i][j]:
            max_step = max([currentMaxStep(data, row, col, x, y), max_step])
    return max_step + 1


# traverse the whole data and generate the max step map
def getMaxMap(data, row, col):
    Map = [[0 for j in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            Map[i][j] = currentMaxStep(data, row, col, i, j)
    print('the max step map is:')
    for i in range(row):
        print(Map[i])
    return Map


# find the max from the max step map
def maxStep(data, row, col):
    Map = getMaxMap(data, row, col)
    return max([max(i) for i in Map])


if __name__ == "__main__":
    re = generate_map(4, 3)
