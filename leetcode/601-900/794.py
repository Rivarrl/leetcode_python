# -*- coding: utf-8 -*-
# ======================================
# @File    : 794.py
# @Time    : 2020/12/27 23:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [794. 有效的井字游戏](https://leetcode-cn.com/problems/valid-tic-tac-toe-state/)
    """
    @timeit
    def validTicTacToe(self, board: List[str]) -> bool:
        x = o = 0
        for row in board:
            for e in row:
                if e == 'X':
                    x += 1
                elif e == 'O':
                    o += 1
        if x - o > 1 or x - o < 0:
            return False
        l3 = 0
        for i in range(3):
            if board[i].count('X') == 3 or board[i].count('O') == 3:
                l3 += 1
        for j in range(3):
            col = board[0][j] + board[1][j] + board[2][j]
            if col.count('X') == 3 or col.count('O') == 3:
                l3 += 1
        d1, d2 = board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]
        if d1.count('X') == 3:
            l3 += 1
        if d2.count('O') == 3:
            l3 += 1
        return l3 <= 1


if __name__ == '__main__':
    a = Solution()
    a.validTicTacToe(board = ["O  ", "   ", "   "])
    a.validTicTacToe(board = ["XOX", " X ", "   "])
    a.validTicTacToe(board = ["XXX", "   ", "OOO"])
    a.validTicTacToe(board = ["XOX", "O O", "XOX"])
    a.validTicTacToe(["XXX","OOX","OOX"])