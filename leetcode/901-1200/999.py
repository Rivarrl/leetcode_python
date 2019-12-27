# -*- coding: utf-8 -*-
# ======================================
# @File    : 999.py
# @Time    : 2019/12/27 11:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [999. 车的可用捕获量](https://leetcode-cn.com/problems/available-captures-for-rook/)
    """
    @timeit
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # 车只有一个，所以就是先找车，再向四个方向穷举搜索
        res = 0
        i, j = [[i,j] for j in range(8) for i in range(8) if board[i][j] == 'R'][0]
        for x in range(i-1, -1, -1):
            if board[x][j] == 'B': break
            if board[x][j] == 'p':
                res += 1
                break
        for x in range(i+1, 8):
            if board[x][j] == 'B': break
            if board[x][j] == 'p':
                res += 1
                break
        for y in range(j-1, -1, -1):
            if board[i][y] == 'B': break
            if board[i][y] == 'p':
                res += 1
                break
        for y in range(j+1, 8):
            if board[i][y] == 'B': break
            if board[i][y] == 'p':
                res += 1
                break
        return res



if __name__ == '__main__':
    a = Solution()
    a.numRookCaptures([[".",".",".",".",".",".",".","."],
                       [".",".",".","p",".",".",".","."],
                       [".",".",".","R",".",".",".","p"],
                       [".",".",".",".",".",".",".","."],
                       [".",".",".",".",".",".",".","."],
                       [".",".",".","p",".",".",".","."],
                       [".",".",".",".",".",".",".","."],
                       [".",".",".",".",".",".",".","."]])
    a.numRookCaptures([[".",".",".",".",".",".",".","."],
                       [".","p","p","p","p","p",".","."],
                       [".","p","p","B","p","p",".","."],
                       [".","p","B","R","B","p",".","."],
                       [".","p","p","B","p","p",".","."],
                       [".","p","p","p","p","p",".","."],
                       [".",".",".",".",".",".",".","."],
                       [".",".",".",".",".",".",".","."]])
    a.numRookCaptures([[".",".",".",".",".",".",".","."],
                       [".",".",".","p",".",".",".","."],
                       [".",".",".","p",".",".",".","."],
                       ["p","p",".","R",".","p","B","."],
                       [".",".",".",".",".",".",".","."],
                       [".",".",".","B",".",".",".","."],
                       [".",".",".","p",".",".",".","."],
                       [".",".",".",".",".",".",".","."]])