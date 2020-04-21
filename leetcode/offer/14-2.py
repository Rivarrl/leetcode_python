# -*- coding: utf-8 -*-
# ======================================
# @File    : 14-2.py
# @Time    : 2020/4/21 15:32
# @Author  : Rivarrl
# ======================================
# [面试题14- II. 剪绳子 II](https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/)

from algorithm_utils import *

class Solution:
    @timeit
    def cuttingRope(self, n: int) -> int:
        # dp
        dp = [1] * (n + 1)
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i-j), dp[i-j] * j)
        return dp[-1] % (10 ** 9 + 7)

if __name__ == '__main__':
    a = Solution()
    a.cuttingRope(2)
    a.cuttingRope(10)