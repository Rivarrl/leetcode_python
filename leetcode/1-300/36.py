# -*- coding: utf-8 -*-
# ======================================
# @File    : 36.py
# @Time    : 2019/11/15 21:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)
    """
    @timeit
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        思路：对每个格子分别入三个set
        """
        col, row, area = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col[i]: return False
                    if board[i][j] in row[j]: return False
                    k = (i // 3) * 3 + j // 3
                    if board[i][j] in area[k]: return False
                    col[i].add(board[i][j])
                    row[j].add(board[i][j])
                    area[k].add(board[i][j])
        return True

if __name__ == '__main__':
    a = Solution()
    a.isValidSudoku([
["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
])

