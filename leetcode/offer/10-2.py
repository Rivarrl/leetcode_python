# -*- coding: utf-8 -*-
# ======================================
# @File    : 10-2.py
# @Time    : 2020/4/21 14:20
# @Author  : Rivarrl
# ======================================
# [面试题10- II. 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)

from algorithm_utils import *

class Solution:
    @timeit
    def numWays(self, n: int) -> int:
        # dp[n] = dp[n-1] + dp[n-2]
        if n <= 1: return 1
        mod = 10 ** 9 + 7
        one = two = 1
        res = 0
        for i in range(2, n+1):
            res = one + two
            one, two = res, one
        return res % mod

if __name__ == '__main__':
    a = Solution()
    a.numWays(2)
    a.numWays(7)