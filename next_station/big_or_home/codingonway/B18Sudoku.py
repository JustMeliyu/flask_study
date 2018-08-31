# encoding: utf-8
"""
求数独
"""


class Val(object):
    def __init__(self, val, alter=False):
        self.val = val
        self.alter = alter

class SudoKu(object):
    def __init__(self):
        self.sudoku = [[0]*9 for _ in range(9)]


sudoku = SudoKu()
sudoku.sudoku[0][0] = Val(3, alter=True)
sudoku.sudoku[0][1] = Val(4, alter=True)
sudoku.sudoku[0][5] = Val(2, alter=True)
sudoku.sudoku[0][7] = Val(1, alter=True)
sudoku.sudoku[0][8] = Val(7, alter=True)
print(sudoku.sudoku)
