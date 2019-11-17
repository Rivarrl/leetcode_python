# -*- coding: utf-8 -*-
# ======================================
# @File    : 5215.py
# @Time    : 2019/11/16 23:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def numberOfWays(self, num_people: int) -> int:
        dp = [0] * (num_people+1)
        dp[0] = 1
        dp[2] = 1
        for i in range(4, num_people+1, 2):
            for j in range(0, i, 2):
                dp[i] += dp[j] * dp[i-2-j]
        return dp[num_people] % (10**9+7)


if __name__ == '__main__':
    a = Solution()
    a.numberOfWays(4)
    a.numberOfWays(6)
    a.numberOfWays(8)