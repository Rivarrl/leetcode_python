# -*- coding: utf-8 -*-
# ======================================
# @File    : 200.py
# @Time    : 2020/4/20 0:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)
    """
    @timeit
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        dxy = ((0,1),(0,-1),(1,0),(-1,0))
        def bfs(i, j):
            stk = [(i, j)]
            while stk:
                a, b = stk.pop(0)
                for dx, dy in dxy:
                    x, y = a + dx, b + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                        grid[x][y] = '0'
                        stk.append((x, y))
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.numIslands([['1','1','1','1','0'],
                  ['1','1','0','1','0'],
                  ['1','1','0','0','0'],
                  ['0','0','0','0','0']])
    a.numIslands([['1','1','0','0','0'],
                  ['1','1','0','0','0'],
                  ['0','0','1','0','0'],
                  ['0','0','0','1','1']])