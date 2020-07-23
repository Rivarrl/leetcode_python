# -*- coding: utf-8 -*-
# ======================================
# @File    : 64.py
# @Time    : 2020/7/23 9:37 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [64. 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)
    """
    @timeit
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, m):
            dp[0][j] += grid[0][j] + dp[0][j-1]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

if __name__ == '__main__':
    a = Solution()
    a.minPathSum([[1,3,1],
                  [1,5,1],
                  [4,2,1]])