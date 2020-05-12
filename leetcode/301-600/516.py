# -*- coding: utf-8 -*-
# ======================================
# @File    : 516.py
# @Time    : 2020/5/11 19:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [516. 最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence/)
    """
    @timeit
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    x = dp[i+1][j-1] if j - i >= 2 else 0
                    dp[i][j] = x + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][-1]

    @timeit
    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            cur = 0
            for j in range(i-1, -1, -1):
                tmp = dp[j]
                if s[j] == s[i]: dp[j] = cur + 2
                cur = max(cur, tmp)
        return max(dp)


if __name__ == '__main__':
    a = Solution()
    a.longestPalindromeSubseq2("bbbab")
    a.longestPalindromeSubseq2("cbbd")