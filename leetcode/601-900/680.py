# -*- coding: utf-8 -*-
# ======================================
# @File    : 680.py
# @Time    : 2020/5/19 21:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [680. 验证回文字符串 Ⅱ](https://leetcode-cn.com/problems/valid-palindrome-ii/)
    """
    @timeit
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
            else:
                s1, s2 = s[l+1:r+1], s[l:r]
                return s1 == s1[::-1] or s2 == s2[::-1]

if __name__ == '__main__':
    a = Solution()
    a.validPalindrome("aba")
    a.validPalindrome("abca")