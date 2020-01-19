# -*- coding: utf-8 -*-
# ======================================
# @File    : 125
# @Time    : 2020/1/11 18:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [125. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)
    """
    @timeit
    def isPalindrome(self, s: str) -> bool:
        def valid(x):
            return x.isalpha() or x.isdigit()
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            while i < j and not valid(s[i]):
                i += 1
            while i < j and not valid(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    a = Solution()
    a.isPalindrome("A man, a plan, a canal: Panama")
    a.isPalindrome("race a car")
    a.isPalindrome("0P")