# -*- coding: utf-8 -*-
# ======================================
# @File    : 01-02.py
# @Time    : 2020/5/9 23:06
# @Author  : Rivarrl
# ======================================
# [面试题 01.02. 判定是否互为字符重排](https://leetcode-cn.com/problems/check-permutation-lcci/)
from algorithm_utils import *
class Solution:
    @timeit
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        from collections import Counter
        d1, d2 = Counter(s1), Counter(s2)
        for c in d2:
            if not c in d1 or d1[c] != d2[c]:
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    a.CheckPermutation("abc", "bca")
    a.CheckPermutation("abc", "bad")