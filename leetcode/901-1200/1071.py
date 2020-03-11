# -*- coding: utf-8 -*-
# ======================================
# @File    : 1071.py
# @Time    : 2020/3/12 0:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        def gcd(a, b):
            if a == 0: return b
            return gcd(b%a, a)
        if str1 + str2 != str2 + str1: return ""
        m, n = len(str1), len(str2)
        return str1[:gcd(n, m)]


    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        # 模拟更相减损术
        n1 = len(str1)
        n2 = len(str2)
        if n1 < n2:
            str1, str2 = str2, str1
        while str2 != "":
            tmp = str1.replace(str2, "")
            if tmp == str1:
                return ""
            str1, str2 = str2, tmp
        return str1


if __name__ == '__main__':
    a = Solution()
    a.gcdOfStrings(str1 = "ABCABC", str2 = "ABC")
    a.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB")
    a.gcdOfStrings(str1 = "LEET", str2 = "CODE")