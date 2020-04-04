# -*- coding: utf-8 -*-
# ======================================
# @File    : 5362.py
# @Time    : 2020/4/4 22:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n: return False
        if k == n: return True
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        res = 0
        for key in d:
            if d[key] & 1:
                res += 1
        return res <= k

if __name__ == '__main__':
    a = Solution()
    a.canConstruct(s = "annabelle", k = 2)
    a.canConstruct(s = "leetcode", k = 3)
    a.canConstruct(s = "true", k = 4)
    a.canConstruct(s = "yzyzyzyzyzyzyzy", k = 2)
    a.canConstruct(s = "cr", k = 7)