# -*- coding: utf-8 -*-
# ======================================
# @File    : 5319.py
# @Time    : 2020/1/26 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "": return 0
        if s == s[::-1]: return 1
        return 2

if __name__ == '__main__':
    a = Solution()
    a.removePalindromeSub("ababa")
    a.removePalindromeSub("abb")
    a.removePalindromeSub("baabb")
    a.removePalindromeSub("")