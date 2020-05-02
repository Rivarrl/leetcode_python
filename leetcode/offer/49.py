# -*- coding: utf-8 -*-
# ======================================
# @File    : 49.py
# @Time    : 2020/5/2 13:13
# @Author  : Rivarrl
# ======================================
# [面试题49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)
from algorithm_utils import *
class Solution:
    @timeit
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        a = b = c = 0
        for i in range(1, n):
            aa, bb, cc = 2 * dp[a], 3 * dp[b], 5 * dp[c]
            x = min(aa, bb, cc)
            if x == aa: a += 1
            if x == bb: b += 1
            if x == cc: c += 1
            dp[i] = x
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    a.nthUglyNumber(10)