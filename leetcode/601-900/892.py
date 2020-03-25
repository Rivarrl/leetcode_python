# -*- coding: utf-8 -*-
# ======================================
# @File    : 892.py
# @Time    : 2020/3/25 8:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [892. 三维形体的表面积](https://leetcode-cn.com/problems/surface-area-of-3d-shapes/)
    """
    @timeit
    def surfaceArea(self, grid: List[List[int]]) -> int:
        lr = fb = ud = 0
        n = len(grid)
        s = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    ud += grid[i][j] - 1
                    s += grid[i][j]
        for i in range(n):
            for j in range(n):
                if j > 0:
                    lr += min(grid[i][j], grid[i][j-1])
                    fb += min(grid[j][i], grid[j-1][i])
        return s * 6 - ((ud + lr + fb) * 2)


if __name__ == '__main__':
    a = Solution()
    a.surfaceArea([[2]])
    a.surfaceArea([[1,2],[3,4]])
    a.surfaceArea([[1,0],[0,2]])
    a.surfaceArea([[1,1,1],[1,0,1],[1,1,1]])
    a.surfaceArea([[2,2,2],[2,1,2],[2,2,2]])