# -*- coding: utf-8 -*-
# ======================================
# @File    : 5527.py
# @Time    : 2020/10/17 23:13
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5527. 大小为 K 的不重叠线段的数目]()
    """
    @timeit
    def numberOfSets(self, N: int, K: int) -> int:
        dp = [[0] * (K+1) for _ in range(N+1)]
        mod = 10 ** 9 + 7
        for n in range(2, N+1):
            dp[n][1] = dp[n-1][1] + n - 1
            for m in range(2, min(n-1, K+1)):
                for i in range(1, n-m+1):
                    dp[n][m] = (dp[n][m] + i * dp[n-i][m-1]) % mod
            if n-1 <= K: dp[n][n-1] = 1
        return dp[N][K] % mod

if __name__ == '__main__':
    a = Solution()
    a.numberOfSets(N = 4, K = 2)
    a.numberOfSets(N = 3, K = 1)
    a.numberOfSets(N = 30, K = 7)
    a.numberOfSets(N = 5, K = 3)
    a.numberOfSets(N = 3, K = 2)
    a.numberOfSets(751, 201)