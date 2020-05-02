# -*- coding: utf-8 -*-
# ======================================
# @File    : 47.py
# @Time    : 2020/5/2 14:00
# @Author  : Rivarrl
# ======================================
# [面试题47. 礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def maxValue(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + grid[i][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + grid[i][j])
        return dp[-1][-1]

if __name__ == '__main__':
    a = Solution()
    a.maxValue([[1,3,1],
                [1,5,1],
                [4,2,1]])