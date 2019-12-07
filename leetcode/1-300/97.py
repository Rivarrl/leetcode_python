# -*- coding: utf-8 -*-
# ======================================
# @File    : 97.py
# @Time    : 2019/11/29 8:52
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [97. 交错字符串](https://leetcode-cn.com/problems/interleaving-string/)
    """
    @timeit
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        思路：动态规划，自顶向下
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        def dfs(i, j, k):
            if i == n1:
                return s2[j:] == s3[k:]
            elif j == n2:
                return s1[i:] == s3[k:]
            if memo[i][j] != None: return memo[i][j]
            memo[i][j] = (s1[i] == s3[k] and dfs(i+1, j, k+1)) or (s2[j] == s3[k] and dfs(i, j+1, k+1))
            return memo[i][j]
        memo = [[None] * n2 for _ in range(n1)]
        return dfs(0, 0, 0)


    @timeit
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        """
        思路：自底向上
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        dp = [[False] * (n2+1) for _ in range(n1+1)]
        dp[0][0] = True
        for i in range(n1):
            dp[i+1][0] = dp[i][0] and s1[i] == s3[i]
        for j in range(n2):
            dp[0][j+1] = dp[0][j] and s2[j] == s3[j]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]


    @timeit
    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        """
        思路：dp，滚动一维数组，每次只需要看左侧i-1和上侧j-1
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        dp = [False] * (n2 + 1)
        for i in range(n1+1):
            for j in range(n2+1):
                if i == j == 0: dp[j] = True
                elif i == 0: dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
                elif j == 0: dp[j] = dp[j] and s1[i-1] == s3[i-1]
                else:
                    dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    a.isInterleave3(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
    a.isInterleave3(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
    a.isInterleave3("", "b", "b")
