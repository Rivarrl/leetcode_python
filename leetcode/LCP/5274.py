# -*- coding: utf-8 -*-
# ======================================
# @File    : 5274.py
# @Time    : 2019/11/24 10:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps//2+1)
        mod = 10**9 + 7
        dp = [[0] * arrLen for _ in range(steps+1)]
        dp[0][0] = 1
        for i in range(steps):
            for j in range(arrLen):
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
                if j > 0: dp[i+1][j-1] = (dp[i+1][j-1] + dp[i][j]) % mod
                if j < arrLen - 1: dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % mod
        return dp[steps][0]


if __name__ == '__main__':
    a = Solution()
    a.numWays(3,2)
    a.numWays(2,4)
    a.numWays(4,2)