# -*- coding: utf-8 -*-
# ======================================
# @File    : 5151.py
# @Time    : 1/25/20 10:40 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5151. 破坏回文串](https://leetcode-cn.com/problems/break-a-palindrome/)
    """
    @timeit
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ""
        palindrome = [e for e in palindrome]
        for i in range(n//2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                break
        else:
            palindrome[-1] = 'a' if palindrome[-1] != 'a' else 'b'
        return ''.join(palindrome)


if __name__ == '__main__':
    a = Solution()
    a.breakPalindrome("abccba")
    a.breakPalindrome("a")
    a.breakPalindrome("zazaz")
    a.breakPalindrome("aaaa")
    a.breakPalindrome("aabaa")