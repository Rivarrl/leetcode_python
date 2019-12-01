# -*- coding: utf-8 -*-
# ======================================
# @File    : 5275.py
# @Time    : 2019/12/1 10:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    5275. 找出井字棋的获胜者
    """
    @timeit
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = len(moves)
        chess = [[-1] * 3 for _ in range(3)]
        # a:0, b:1
        d = ["A", "B"]
        for k in range(n):
            i, j = moves[k]
            chess[i][j] = k % 2
        # row/col
        for i in range(3):
            if chess[i][0] != -1 and chess[i][0] == chess[i][1] == chess[i][2]: return d[chess[i][0]]
            if chess[0][i] != -1 and chess[0][i] == chess[1][i] == chess[2][i]: return d[chess[0][i]]
        if chess[0][0] != -1 and chess[0][0] == chess[1][1] == chess[2][2]: return d[chess[0][0]]
        if chess[0][2] != -1 and chess[0][2] == chess[1][1] == chess[2][0]: return d[chess[0][2]]
        if n == 9: return "Draw"
        return "Pending"





if __name__ == '__main__':
    a = Solution()
    a.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])
    a.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])
    a.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])
    a.tictactoe([[0,0],[1,1]])