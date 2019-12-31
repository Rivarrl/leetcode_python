# -*- coding: utf-8 -*-
# ======================================
# @File    : 883.py
# @Time    : 2019/12/31 19:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def projectionArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        s1 = s2 = s3 = 0
        for i in range(n):
            r = 0
            for j in range(m):
                if grid[i][j] == 0: continue
                r = max(r, grid[i][j])
                s1 += 1
            s2 += r
        for j in range(m):
            r = 0
            for i in range(n):
                r = max(r, grid[i][j])
            s3 += r
        return s1 + s2 + s3


if __name__ == '__main__':
    a = Solution()
    a.projectionArea([[2]])
    a.projectionArea([[1,2],[3,4]])
    a.projectionArea([[1,0],[0,2]])
    a.projectionArea([[1,1,1],[1,0,1],[1,1,1]])
    a.projectionArea([[2,2,2],[2,1,2],[2,2,2]])