# -*- coding: utf-8 -*-
# ======================================
# @File    : 629.py
# @Time    : 2020/12/16 7:32 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [629. K个逆序对数组](https://leetcode-cn.com/problems/k-inverse-pairs-array/)
    """
    @timeit
    def kInversePairs(self, n: int, k: int) -> int:
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-1][j-i+1]
        # dp[i][j+1] = dp[i-1][j+1] + dp[i-1][j] + dp[i-1][j-1] + ... + dp[i-1][j-i+2]
        # dp[i][j+1] - dp[i][j] = dp[i-1][j+1] - dp[i-1][j-i+1]
        # dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i]
        mod = 10 ** 9 + 7
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                if j >= i:
                    dp[i][j] -= dp[i - 1][j - i]
                dp[i][j] %= mod
        return dp[n][k]

if __name__ == '__main__':
    a = Solution()
    a.kInversePairs(3, 0)
    a.kInversePairs(3, 1)
    a.kInversePairs(1000, 500)