# -*- coding: utf-8 -*-
# ======================================
# @File    : 5417.py
# @Time    : 2020/5/24 10:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5417. 定长子串中元音的最大数目]()
    """
    @timeit
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        ctr = 0
        for i in range(min(n, k)):
            if s[i] in 'aeiou': ctr += 1
        res = ctr
        for i in range(n-k):
            j = i + k
            if s[i] in 'aeiou': ctr -= 1
            if s[j] in 'aeiou': ctr += 1
            res = max(res, ctr)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxVowels(s = "abciiidef", k = 3)
    a.maxVowels(s = "aeiou", k = 2)
    a.maxVowels(s = "leetcode", k = 3)
    a.maxVowels(s = "rhythms", k = 4)
    a.maxVowels(s = "tryhard", k = 4)