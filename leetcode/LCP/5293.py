# -*- coding: utf-8 -*-
# ======================================
# @File    : 5293.py
# @Time    : 2019/12/22 10:48
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5293. 子串的最大出现次数](https://leetcode-cn.com/problems/maximum-number-of-occurrences-of-a-substring/)
    """
    @timeit
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        h = {}
        for i in range(len(s)-minSize+1):
            c = s[i:i+minSize]
            if len(set(c)) > maxLetters: continue
            h[c] = h.get(c, 0) + 1
        return 0 if not h else max(h.values())


if __name__ == '__main__':
    a = Solution()
    a.maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4)
    a.maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3)
    a.maxFreq(s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3)
    a.maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3)