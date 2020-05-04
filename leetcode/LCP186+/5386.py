# -*- coding: utf-8 -*-
# ======================================
# @File    : 5386.py
# @Time    : 2020/5/2 22:42
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    # @timeit
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted([e for e in s1]))
        s2 = ''.join(sorted([e for e in s2]))
        if s1 < s2: return self.checkIfCanBreak(s2, s1)
        for c1, c2 in zip(s1, s2):
            if c1 < c2:
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    x= a.checkIfCanBreak(s1 = "abc", s2 = "xya")
    print(x)
    x= a.checkIfCanBreak(s1 = "abe", s2 = "acd")
    print(x)
    x= a.checkIfCanBreak(s1 = "leetcodee", s2 = "interview")
    print(x)
