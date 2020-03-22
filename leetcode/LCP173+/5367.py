# -*- coding: utf-8 -*-
# ======================================
# @File    : 5367.py
# @Time    : 2020/3/22 10:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5367. 最长快乐前缀](https://leetcode-cn.com/problems/longest-happy-prefix/)
    """
    @timeit
    def longestPrefix(self, s: str) -> str:
        res = ''
        pre = ''
        suf = ''
        n = len(s)
        for i in range(n-1):
            pre += s[i]
            j = n - 1 - i
            suf = s[j] + suf
            if suf == pre:
                res = pre
        return res

    @timeit
    def longestPrefix2(self, s: str) -> str:
        n = len(s)
        nxt = [0] * (n + 1)
        i, j = 0, -1
        nxt[0] = -1
        while i < n:
            if j == -1 or s[j] == s[i]:
                nxt[i+1] = j + 1
                i += 1
                j += 1
            else:
                j = nxt[j]
        return s[:nxt[n]]


if __name__ == '__main__':
    a = Solution()
    a.longestPrefix2(s = "level")
    a.longestPrefix2(s = "ababab")
    a.longestPrefix2(s = "leetcodeleet")
    a.longestPrefix2(s = "a")
    a.longestPrefix2("aaaaa")
