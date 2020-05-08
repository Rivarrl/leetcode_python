# -*- coding: utf-8 -*-
# ======================================
# @File    : 221.py
# @Time    : 2020/5/8 15:14
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [221. 最大正方形](https://leetcode-cn.com/problems/maximal-square/)
    """
    @timeit
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
        return max(max(e) for e in dp) ** 2

if __name__ == '__main__':
    a = Solution()
    a.maximalSquare([['1', '0', '1', '0', '0'],
                     ['1', '0', '1', '1', '1'],
                     ['1', '1', '1', '1', '1'],
                     ['1', '0', '0', '1', '0']])