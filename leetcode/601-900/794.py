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
        def can_win(x):
            return (board[0][0] == x and board[0][1] == x and board[0][2] == x) \
                   or (board[1][0] == x and board[1][1] == x and board[1][2] == x) \
                   or (board[2][0] == x and board[2][1] == x and board[2][2] == x) \
                   or (board[0][0] == x and board[1][0] == x and board[2][0] == x) \
                   or (board[0][1] == x and board[1][1] == x and board[2][1] == x) \
                   or (board[0][2] == x and board[1][2] == x and board[2][2] == x) \
                   or (board[0][0] == x and board[1][1] == x and board[2][2] == x) \
                   or (board[0][2] == x and board[1][1] == x and board[2][0] == x)

        if x - o > 1 or x - o < 0:
            return False

        if can_win('X') and x == o:
            return False
        if can_win('O') and x > o:
            return False
        return True


if __name__ == '__main__':
    a = Solution()
    a.validTicTacToe(board = ["O  ", "   ", "   "])
    a.validTicTacToe(board = ["XOX", " X ", "   "])
    a.validTicTacToe(board = ["XXX", "   ", "OOO"])
    a.validTicTacToe(board = ["XOX", "O O", "XOX"])
    a.validTicTacToe(["XXX","OOX","OOX"])