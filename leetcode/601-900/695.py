# -*- coding: utf-8 -*-
# ======================================
# @File    : 695.py
# @Time    : 2020/3/15 0:08
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/)
    """
    @timeit
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        res = 0
        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        def dfs(i, j):
            r = 1
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and vis[x][y] == 0 and grid[x][y] == 1:
                    vis[x][y] = 1
                    r += dfs(x, y)
            return r

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    vis[i][j] = 1
                    res = max(res, dfs(i, j))
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,1,1,0,1,0,0,0,0,0,0,0,0],
                       [0,1,0,0,1,1,0,0,1,0,1,0,0],
                       [0,1,0,0,1,1,0,0,1,1,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,1,0,0],
                       [0,0,0,0,0,0,0,1,1,1,0,0,0],
                       [0,0,0,0,0,0,0,1,1,0,0,0,0]])