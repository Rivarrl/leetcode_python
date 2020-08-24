# -*- coding: utf-8 -*-
# ======================================
# @File    : 459.py
# @Time    : 2020/8/24 9:45 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s*2)[1:-1]

if __name__ == '__main__':
    a = Solution()
    a.repeatedSubstringPattern("abab")
    a.repeatedSubstringPattern("aba")
    a.repeatedSubstringPattern("abcabcabcabc")