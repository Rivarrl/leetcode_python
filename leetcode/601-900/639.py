# -*- coding: utf-8 -*-
# ======================================
# @File    : 639.py
# @Time    : 2020/6/24 22:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [639. 解码方法 2](https://leetcode-cn.com/problems/decode-ways-ii/)
    """
    @timeit
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else 1
        mod = 10 ** 9 + 7
        for i in range(1, n):
            if s[i] == '*':
                dp[i+1] = dp[i] * 9
                if s[i-1] == '1':
                    dp[i+1] += dp[i-1] * 9
                elif s[i-1] == '2':
                    dp[i+1] += dp[i-1] * 6
                elif s[i-1] == '*':
                    dp[i+1] += dp[i-1] * 15
            elif s[i] == '0':
                if s[i-1] in {'1', '2'}:
                    dp[i+1] = dp[i-1]
                elif s[i-1] == '*':
                    dp[i+1] = dp[i-1] * 2
                else:
                    return 0
            else:
                if s[i-1] == '*':
                    dp[i+1] = dp[i] + dp[i-1]
                    if int(s[i]) <= 6:
                        dp[i+1] += dp[i-1]
                else:
                    dp[i+1] = dp[i]
                    if 10 <= int(s[i-1:i+1]) <= 26:
                        dp[i+1] += dp[i-1]
        return dp[-1] % mod


if __name__ == '__main__':
    a = Solution()
    a.numDecodings("*")
    a.numDecodings("1*")
    a.numDecodings("*1")
    a.numDecodings("**1**")