# -*- coding: utf-8 -*-
# ======================================
# @File    : 5257.py
# @Time    : 2019/11/10 11:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        5257. 统计封闭岛屿的数目
        """
        def dfs(i, j):
            if i < 0 or j < 0 or i == n or j == m or grid[i][j] == 1: return
            grid[i][j] = 1
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                dfs(x, y)
            return True

        n = len(grid)
        if n <= 2: return 0
        m = len(grid[0])
        if m <= 2: return 0
        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        res = 0
        for i in range(n):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][m-1] == 0:
                dfs(i, m-1)
        for j in range(m):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[n-1][j] == 0:
                dfs(n-1, j)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j)
                    res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    m1 = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    sol.closedIsland(m1)
    m2 = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    sol.closedIsland(m2)
    m3 = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
    sol.closedIsland(m3)
    m4 = [[0,0,1,1,0,1,0,0,1,0],
          [1,1,0,1,1,0,1,1,1,0],
          [1,0,1,1,1,0,0,1,1,0],
          [0,1,1,0,0,0,0,1,0,1],
          [0,0,0,0,0,0,1,1,1,0],
          [0,1,0,1,0,1,0,1,1,1],
          [1,0,1,0,1,1,0,0,0,1],
          [1,1,1,1,1,1,0,0,0,0],
          [1,1,1,0,0,1,0,1,0,1],
          [1,1,1,0,1,1,0,1,1,0]]
    sol.closedIsland(m4)
    m5 = [[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1],[0,1,1,1,0]]
    matrix_pretty_print(m5)
    sol.closedIsland(m5)
    # 2 1 2 5
