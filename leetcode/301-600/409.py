# -*- coding: utf-8 -*-
# ======================================
# @File    : 409.py
# @Time    : 2020/3/19 10:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        res = 0
        p = 0
        for k, v in d.items():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                p = 1
        return res + p

if __name__ == '__main__':
    a = Solution()
    a.longestPalindrome("abccccdd")