# -*- coding: utf-8 -*-
# ======================================
# @File    : 514.py
# @Time    : 2020/11/11 9:32 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [514. 自由之路](https://leetcode-cn.com/problems/freedom-trail/)
    """
    @timeit
    def findRotateSteps(self, ring: str, key: str) -> int:
        # dp[i][j] key第j字符在ring第i个字符停留时的最小值
        # dp[i][j] = min(min(abs(i-k), n-abs(i-k)) + dp[k][j-1] for k in range(n) if ring[k] == key[j-1])
        n, m = len(ring), len(key)
        dp = [[10001] * m for _ in range(n)]
        for j in range(m):
            for i in range(n):
                if ring[i] == key[j]:
                    if j == 0:
                        dp[i][0] = min(i, n - i)
                    else:
                        for k in range(n):
                            if ring[k] == key[j - 1]:
                                dp[i][j] = min(dp[i][j], min(abs(i-k), n-abs(i-k)) + dp[k][j-1])
        res = 10001
        for i in range(n):
            if key[-1] == ring[i]:
                res = min(res, dp[i][-1])
        return res + m

if __name__ == '__main__':
    a = Solution()
    a.findRotateSteps(ring = "godding", key = "gd")
    a.findRotateSteps("edcba", "abcde")