# -*- coding: utf-8 -*-
# ======================================
# @File    : 1573.py
# @Time    : 2020/9/9 23:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1573. 分割字符串的方案数](https://leetcode-cn.com/problems/number-of-ways-to-split-a-string/)
    """
    @timeit
    def numWays(self, s: str) -> int:
        mod = 1000000007
        pre = {}
        c = 0
        n = len(s)
        for x in s:
            if x == '1':
                c += 1
            pre[c] = pre.get(c, 0) + 1
        if c % 3 > 0: return 0
        if c == 0: # C(2,n)
            return ((n-1) * (n-2) // 2) % mod
        res = 1
        for i in range(1, c):
            if i % (c // 3) == 0:
                res *= pre[i]
        return res % mod

if __name__ == '__main__':
    a = Solution()
    a.numWays(s = "10101")
    a.numWays(s = "1001")
    a.numWays(s = "0000")
    a.numWays(s = "100100010100110")
    a.numWays("101100111111")