# -*- coding: utf-8 -*-
# ======================================
# @File    : 463.py
# @Time    : 2020/10/30 1:10 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        res = 0
        def lrud(i, j):
            res = 0
            if i > 0: res += grid[i-1][j]
            if j > 0: res += grid[i][j-1]
            if i < n-1: res += grid[i+1][j]
            if j < m-1: res += grid[i][j+1]
            return res
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    res += 4 - lrud(i, j)
        return res

    @timeit
    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        from scipy.signal import convolve2d
        return int(abs(convolve2d(grid, [[1,-2],[0,1]])).sum())


if __name__ == '__main__':
    a = Solution()
    a.islandPerimeter2([[0,1,0,0],
                     [1,1,1,0],
                     [0,1,0,0],
                     [1,1,0,0]])