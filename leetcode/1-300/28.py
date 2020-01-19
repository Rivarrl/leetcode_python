# -*- coding: utf-8 -*-
# ======================================
# @File    : 28
# @Time    : 2020/1/11 22:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)
    KMP算法
    """
    @timeit
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(haystack)
        nl = len(needle)
        if nl > l: return -1
        if haystack == needle: return 0
        if nl == 0: return 0
        f = [-1] * nl
        k = -1
        for j in range(1, nl):
            while k > -1 and needle[k + 1] != needle[j]:
                k = f[k]
            if needle[k + 1] == needle[j]:
                k += 1
            f[j] = k
        i, j = 0, 0
        while i < l and j < nl:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = f[j - 1] + 1
        return i - nl if j == nl else -1


if __name__ == '__main__':
    a = Solution()
    a.strStr(haystack = "hello", needle = "ll")
    a.strStr(haystack = "aaaaa", needle = "bba")