# -*- coding: utf-8 -*-
# ======================================
# @File    : 934.py
# @Time    : 2020/6/5 16:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [934. 最短的桥](https://leetcode-cn.com/problems/shortest-bridge/)
    """
    @timeit
    def shortestBridge(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        stk = []
        vis = [[False] * m for _ in range(n)]
        def dfs(i, j):
            A[i][j] = 2
            stk.append((i, j, 0))
            for dx, dy in ((1, 0), (0, 1), (0, -1), (-1, 0)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and A[x][y] == 1:
                    dfs(x, y)
        k = 0
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    dfs(i, j)
                    k = 1
                    break
            if k: break
        while stk:
            i, j, s = stk.pop(0)
            for dx, dy in ((1, 0), (0, 1), (0, -1), (-1, 0)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and not vis[x][y]:
                    if A[x][y] == 1: return s
                    vis[x][y] = True
                    if A[x][y] == 0: stk.append((x, y, s+1))

if __name__ == '__main__':
    a = Solution()
    a.shortestBridge([[0,1],[1,0]])
    a.shortestBridge([[0,1,0],[0,0,0],[0,0,1]])
    a.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])