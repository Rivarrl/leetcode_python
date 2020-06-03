# -*- coding: utf-8 -*-
# ======================================
# @File    : 837.py
# @Time    : 2020/6/3 16:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0: return 1.0
        dp = [0.0] * (K + W)
        for i in range(W):
            if K + i > N: break
            dp[K+i] = 1.0
        dp[K-1] = min(W, N-K+1) / W
        for x in range(K-1, 0, -1):
            dp[x-1] = dp[x] + dp[x] / W - dp[x+W] / W
        return dp[0]

if __name__ == '__main__':
    a = Solution()
    a.new21Game(10, 1, 10)
    a.new21Game(6, 1, 10)
    a.new21Game(21, 17, 10)