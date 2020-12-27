# -*- coding: utf-8 -*-
# ======================================
# @File    : 5210.py
# @Time    : 2020/12/27 12:43
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5210. 球会落何处]()
    """
    @timeit
    def findBall(self, grid: List[List[int]]) -> List[int]:
        from functools import lru_cache
        n, m = len(grid), len(grid[0])
        @lru_cache(None)
        def f(i, j):
            if i == n: return j
            if grid[i][j] == 1 and j < m - 1 and grid[i][j+1] == 1:
                return f(i+1, j+1)
            if grid[i][j] == -1 and j > 0 and grid[i][j-1] == -1:
                return f(i+1, j-1)
            return -1
        return [f(0, j) for j in range(m)]

if __name__ == '__main__':
    a = Solution()
    a.findBall(grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]])
    a.findBall(grid = [[-1]])