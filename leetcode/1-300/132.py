# -*- coding: utf-8 -*-
# ======================================
# @File    : 132
# @Time    : 2021/3/8 9:45
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [132. 分割回文串 II](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)
    """
    @timeit
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        dp2 = list(range(len(s)))
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if j == 0:
                        dp2[i] = 0
                    else:
                        dp2[i] = min(dp2[i], dp2[j - 1] + 1)
        return dp2[-1]

if __name__ == '__main__':
    a = Solution()
    a.minCut(s = "aab")
    a.minCut(s = "a")
    a.minCut(s = "ab")