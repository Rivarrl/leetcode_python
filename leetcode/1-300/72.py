# -*- coding: utf-8 -*-
# ======================================
# @File    : 72.py
# @Time    : 2020/4/6 0:51
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0x3f3f3f3f] * (m+1) for _ in range(n+1)]
        for i in range(m+1):
            dp[0][i] = i
        for i in range(n+1):
            dp[i][0] = i
        for i in range(n):
            for j in range(m):
                x = 1 if word1[i] != word2[j] else 0
                dp[i+1][j+1] = min(dp[i][j]+x, dp[i][j+1]+1, dp[i+1][j]+1)
        return dp[-1][-1]


if __name__ == '__main__':
    a = Solution()
    a.minDistance("horse", "ros")
    a.minDistance("intention", "execution")
    a.minDistance("zoologicoarchaeologist", "zoogeologist")