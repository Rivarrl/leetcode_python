# -*- coding: utf-8 -*-
# ======================================
# @File    : 1616.py
# @Time    : 2020/10/12 1:13 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1616. 分割两个字符串得到回文串](https://leetcode-cn.com/problems/split-two-strings-to-make-palindrome/)
    """
    @timeit
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        def check(s):
            for i in range(n//2):
                if s[i] != s[n-1-i]: return False
            return True
        if check(a) or check(b): return True
        for i in range(n):
            if a[i] != b[n-1-i] and a[i] != a[n-1-i] and b[i] != a[n-1-i] and b[i] != b[n-1-i]:
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    a.checkPalindromeFormation(a = "x", b = "y")
    a.checkPalindromeFormation(a = "ulacfd", b = "jizalu")
    a.checkPalindromeFormation("xbdef", "xecab")
