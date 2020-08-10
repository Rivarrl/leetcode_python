# -*- coding: utf-8 -*-
# ======================================
# @File    : 130.py
# @Time    : 2020/8/11 0:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)
    """
    def solve(self, board: List[List[str]]) -> None:
        # 从边缘染色，然后再标记回来
        from collections import deque
        n = len(board)
        if n <= 2: return
        m = len(board[0])
        if m <= 2: return
        def mkp(i, j):
            if board[i][j] == 'O':
                stk.append((i, j))
                board[i][j] = 'P'
        stk = deque()
        for i in range(n):
            mkp(i, 0)
            mkp(i, m-1)
        for j in range(m):
            mkp(0, j)
            mkp(n-1, j)
        while stk:
            i, j = stk.popleft()
            for ni, nj in ((i,j+1), (i, j-1), (i+1, j), (i-1, j)):
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 'O':
                    mkp(ni, nj)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'P':
                    board[i][j] = 'O'


if __name__ == '__main__':
    a = Solution()
    x = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    a.solve(x)
    matrix_pretty_print(x)