# -*- coding: utf-8 -*-
# ======================================
# @File    : 392.py
# @Time    : 2020/7/27 0:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]:
                j += 1
            if j == len(s): return True
        return False

if __name__ == '__main__':
    a = Solution()
    a.isSubsequence("abc", "ahbgdc")
    a.isSubsequence("axc", "ahbgdc")
