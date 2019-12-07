# -*- coding: utf-8 -*-
# ======================================
# @File    : 5278.py
# @Time    : 2019/12/1 10:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5278. 分割回文串 III
    dp[i][j]表示s[:i]切j刀的最小代价
    dp[i][j] = min(dp[k][j-1] + cost(s[k:i]) for k in range(i))
    """
    @timeit
    def palindromePartition(self, s: str, k: int) -> int:
        # 不加lru_cache是O(n^4)，加上是O(n^3)
        from functools import lru_cache
        n = len(s)
        if n <= k: return 0
        dp = [[0] * k for _ in range(n)]
        @lru_cache(None)
        def cost(l, r):
            c = 0
            while l < r:
                if s[l] != s[r]: c+=1
                l += 1
                r -= 1
            return c
        inf = 0x3f3f3f3f
        for j in range(k):
            for i in range(n):
                if j == 0:
                    dp[i][j] = cost(0, i)
                else:
                    c = inf
                    for p in range(i):
                        c = min(c, dp[p][j-1] + cost(p+1, i))
                    dp[i][j] = c
        return dp[-1][-1]


    @timeit
    def palindromePartition2(self, s: str, k: int) -> int:
        # 不用lru_cache版O(n^3)
        n = len(s)
        if n <= k: return 0
        dp = [[-1] * k for _ in range(n)]
        def cost(l, r):
            c = 0
            while l < r:
                if s[l] != s[r]: c+=1
                l += 1
                r -= 1
            return c
        for i in range(n):
            dp[i][0] = cost(0, i)
            for p in range(i):
                co = cost(p+1, i)
                for j in range(1, k):
                    if dp[p][j - 1] == -1: continue
                    c = dp[p][j-1] + co
                    if dp[i][j] == -1:
                        dp[i][j] = c
                    else:
                        dp[i][j] = min(dp[i][j], c)
        return dp[-1][-1]


if __name__ == '__main__':
    a = Solution()
    a.palindromePartition("abc", 2)
    a.palindromePartition("aabbc",3)
    a.palindromePartition("leetcode",8)
