# -*- coding: utf-8 -*-
# ======================================
# @File    : 509.py
# @Time    : 2019/11/16 18:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)
    """
    @timeit
    def fib(self, N: int) -> int:
        """
        思路：动态规划
        """
        # 自顶向下，记忆化搜索（慢）
        def f(x):
            if x == 0: return 0
            if x == 1 or x == 2:
                dp[x] = 1
                return 1
            if dp[x] > 0: return dp[x]
            x1, x2 = f(x-1), f(x-2)
            dp[x] = x1 + x2
            return dp[x]

        dp = [0] * (N + 1)
        return f(N)

    @timeit
    def fib2(self, N: int) -> int:
        # 自底向上，动态规划（快）
        if N == 0: return 0
        x1, x2 = 1, 0
        for i in range(1, N):
            x1, x2 = x1 + x2, x1
        return x1

if __name__ == '__main__':
    a = Solution()
    a.fib(30)
    a.fib2(30)