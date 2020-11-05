# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-04.py
# @Time    : 2020/11/5 6:20 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.04. 井字游戏](https://leetcode-cn.com/problems/tic-tac-toe-lcci/)
    """
    @timeit
    def tictactoe(self, board: List[str]) -> str:
        n = len(board)
        def win(s):
            rlist = board[:]
            rlist.extend([''.join([board[i][j] for i in range(n)]) for j in range(n)])
            rlist.append(''.join([board[i][i] for i in range(n)]))
            rlist.append(''.join([board[i][n-1-i] for i in range(n)]))
            return s*n in rlist
        if win('X'): return 'X'
        if win('O'): return 'O'
        if sum(row.count(' ') for row in board) == 0:
            return "Draw"
        return "Pending"

if __name__ == '__main__':
    a = Solution()
    a.tictactoe(board = ["O X"," XO","X O"])
    a.tictactoe(board = ["OOX","XXO","OXO"])
    a.tictactoe(board = ["OOX","XXO","OX "])