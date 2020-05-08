# -*- coding: utf-8 -*-
# ======================================
# @File    : 567.py
# @Time    : 2020/5/8 20:48
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/)
    """
    @timeit
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        need = Counter(s1)
        d = {}
        l = r = ctr = 0
        n = len(s2)
        while r < n:
            c = s2[r]
            if not c in need:
                l = r + 1
                d.clear()
                ctr = 0
            else:
                d[c] = d.get(c, 0) + 1
                if d[c] == need[c]:
                    ctr += 1
                elif d[c] > need[c]:
                    while l < r and s2[l] != c:
                        d[s2[l]] -= 1
                        if d[s2[l]] == need[s2[l]] - 1: ctr -= 1
                        l += 1
                if ctr == len(need): return True
            r += 1
        return False

if __name__ == '__main__':
    a = Solution()
    a.checkInclusion(s1 = "ab", s2 = "eidbaooo")
    a.checkInclusion(s1 = "ab", s2 = "eidboaoo")