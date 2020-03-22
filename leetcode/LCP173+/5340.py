# -*- coding: utf-8 -*-
# ======================================
# @File    : 5340.py
# @Time    : 2020/2/16 10:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5340. 统计有序矩阵中的负数](https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix/)
    """
    @timeit
    def countNegatives(self, grid: List[List[int]]) -> int:
        ctr = 0
        for a in grid:
            for b in a:
                if b < 0:
                    ctr += 1
        return ctr

if __name__ == '__main__':
    a = Solution()
    a.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    a.countNegatives([[3,2],[1,0]])
    a.countNegatives([[1,-1],[-1,-1]])
    a.countNegatives([[-1]])