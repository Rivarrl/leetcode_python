# -*- coding: utf-8 -*-
# ======================================
# @File    : 3.py
# @Time    : 2020/9/12 15:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        dp = [[0] * n for _ in range(3)]
        dp[0][0] = 0 if leaves[0] == 'r' else 1
        for i in range(1, n):
            if leaves[i] == 'r':
                dp[0][i] = dp[0][i-1]

if __name__ == '__main__':
    a = Solution()
    a.minimumOperations(leaves = "rrryyyrryyyrr")
    a.minimumOperations(leaves = "ryr")