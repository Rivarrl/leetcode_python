# -*- coding: utf-8 -*-
# ======================================
# @File    : 214.py
# @Time    : 2020/8/30 0:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [214. 最短回文串](https://leetcode-cn.com/problems/shortest-palindrome/)
    """
    @timeit
    def shortestPalindrome(self, s: str) -> str:
        # KMP
        def fail(s, f):
            f[0] = 0
            f[1] = 0
            for i in range(1, len(s)):
                j = f[i]
                while j and s[i] != s[j]:
                    j = f[j]
                f[i+1] = j+1 if s[i] == s[j] else 0
        n = len(s)
        if n <= 1: return s
        r = s[::-1]
        sr = s + "#" + r
        f = [0] * (len(sr) + 1)
        fail(sr, f)
        return r[:len(r) - f[len(sr)]] + s

    def shortestPalindrome2(self, s: str) -> str:
        # Manacher
        n = len(s)
        if n < 2: return s
        t = "$#"
        for i in range(n):
            t += s[i]
            t += "#"
        p = [0] * (len(t) + 5)
        max_i = 0
        center, right = 0, 0
        window = 1
        for i in range(1, len(t)):
            if i<right:
                p[i] = min(p[2*center - i], right - i)
            while i + p[i] < len(t) and i - p[i] >= 1 and t[i+p[i]] == t[i-p[i]]:
                p[i] += 1
            if p[i] > p[max_i]:
                max_i = i
            if i + p[i] > right:
                right = i + p[i]
                center = i
            if (max_i - p[max_i]) // 2 == 0:
                window = max(window, p[max_i] - 1)
        if window == n: return s
        return s[window:][::-1] + s

if __name__ == '__main__':
    a = Solution()
    a.shortestPalindrome("aacecaaa")
    a.shortestPalindrome("abcd")