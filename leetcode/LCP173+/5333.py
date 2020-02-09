# -*- coding: utf-8 -*-
# ======================================
# @File    : 5333.py
# @Time    : 2020/2/9 10:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5333. 制造字母异位词的最小步骤数](https://leetcode-cn.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/)
    """
    @timeit
    def minSteps(self, s: str, t: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            if c in d and d[c] > 0:
                d[c] -= 1
        return sum(d.values())

if __name__ == '__main__':
    a = Solution()
    a.minSteps(s = "bab", t = "aba")
    a.minSteps(s = "leetcode", t = "practice")
    a.minSteps(s = "anagram", t = "mangaar")
    a.minSteps(s = "xxyyzz", t = "xxyyzz")
    a.minSteps(s = "friend", t = "family")