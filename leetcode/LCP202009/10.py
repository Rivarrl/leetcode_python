# -*- coding: utf-8 -*-
# ======================================
# @File    : 10.py
# @Time    : 2020/9/19 17:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def keyboard(self, k: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(k+1)]
        for j in range(1, n+1):
            for i in range():
                dp[i][j] = dp[i-1][j]

if __name__ == '__main__':
    a = Solution()
    a.keyboard(k = 1, n = 1)
    a.keyboard(k = 1, n = 2)