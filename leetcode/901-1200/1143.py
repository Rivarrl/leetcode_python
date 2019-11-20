# -*- coding: utf-8 -*-
# ======================================
# @File    : 1143.py
# @Time    : 2019/11/20 10:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)
    """
    @timeit
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        思路：动态规划，dp[i][j]表示text[:i]与text[:j]的lcs
        如果text1[i-1] == text2[j-1]，dp[i][j] = dp[i-1][j-1] + 1，否则dp[i][j] = dp[i-1][j-1]
        """
        n, m = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = max(dp[i][j] + int(text1[i] == text2[j]), dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]


    @timeit
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        """
        压缩一下dp数组，用一维数组即可，想象成一个扁长的二维dp状态转移的过程，遍历是从上到下，再从左到右。
        每次状态转移需要为下一次状态转移保存左，上，左上三个变量。
        """
        n, m = len(text1), len(text2)
        if n < m:
            n, m = m, n
            text2, text1 = text1, text2
        dp = [0] * m
        for i in range(n):
            top = left_top = 0
            for j in range(m):
                left = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = left_top + 1
                else:
                    dp[j] = max(left, top)
                top, left_top = dp[j], left
        return dp[-1]


if __name__ == '__main__':
    a = Solution()
    a.longestCommonSubsequence2("abcde", "ace")
    a.longestCommonSubsequence2("abc", "def")
    a.longestCommonSubsequence2("ezupkr", "ubmrapg")
