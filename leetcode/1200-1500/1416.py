# -*- coding: utf-8 -*-
# ======================================
# @File    : 1416.py
# @Time    : 2020/4/24 20:14
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [1] + [0] * n
        for i in range(1, n+1):
            for j in range(i-1, -1, -1):
                if s[j] == '0': continue
                if int(s[j:i]) <= k:
                    dp[i] += dp[j]
                else:
                    if s[i-1] == '0' and dp[i] == 0: return 0
                    break
            dp[i] %= mod
        return dp[-1] % mod

if __name__ == '__main__':
    a = Solution()
    a.numberOfArrays(s = "1000", k = 10000)
    a.numberOfArrays(s = "1000", k = 10)
    a.numberOfArrays(s = "1317", k = 2000)
    a.numberOfArrays(s = "2020", k = 30)
    a.numberOfArrays(s = "1234567890", k = 90)