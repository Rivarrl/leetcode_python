# -*- coding: utf-8 -*-
# ======================================
# @File    : 120.py
# @Time    : 2020/7/14 10:10 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [120. 三角形最小路径和](https://leetcode-cn.com/problems/triangle/)
    """
    @timeit
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, j):
            if i == len(triangle): return 0
            return triangle[i][j] + min(dfs(i+1, j), dfs(i+1, j+1))
        return dfs(0, 0)

if __name__ == '__main__':
    a = Solution()
    a.minimumTotal([[2],
                   [3,4],
                  [6,5,7],
                 [4,1,8,3]])