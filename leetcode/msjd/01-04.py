# -*- coding: utf-8 -*-
# ======================================
# @File    : 01-04.py
# @Time    : 2020/5/9 23:37
# @Author  : Rivarrl
# ======================================
# [面试题 01.04. 回文排列](https://leetcode-cn.com/problems/palindrome-permutation-lcci/)
from algorithm_utils import *

class Solution:
    @timeit
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}
        for x in s:
            d[x] = d.get(x, 0) + 1
        e = 0
        for k, v in d.items():
            if v & 1: e += 1
            if e > 1: return False
        return True

if __name__ == '__main__':
    a = Solution()
    a.canPermutePalindrome("tactcoa")