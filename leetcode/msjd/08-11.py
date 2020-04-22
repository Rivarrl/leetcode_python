# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-11.py
# @Time    : 2020/4/23 0:19
# @Author  : Rivarrl
# ======================================
# [面试题 08.11. 硬币](https://leetcode-cn.com/problems/coin-lcci/)
from algorithm_utils import *

class Solution:
    @timeit
    def waysToChange(self, n: int) -> int:
        dp = {}
        dp[0] = 1
        for i in (1, 5, 10, 25):
            for j in range(i, n+1):
                dp[j] = dp.get(j, 0) + dp[j-i]
        return dp[n] % (10 ** 9 + 7)


if __name__ == '__main__':
    a = Solution()
    a.waysToChange(5)
    a.waysToChange(10)