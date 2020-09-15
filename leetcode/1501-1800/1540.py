# -*- coding: utf-8 -*-
# ======================================
# @File    : 1540.py
# @Time    : 2020/9/15 12:50 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1540. K 次操作转变字符串]()
    """
    @timeit
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        n = len(s)
        a = [k // 26] * 26
        for i in range(1, k%26+1):
            a[i] += 1
        for i in range(n):
            x = ord(t[i]) - ord(s[i])
            if x != 0: a[x] -= 1
            if a[x] < 0:
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    a.canConvertString(s = "input", t = "ouput", k = 9)
    a.canConvertString(s = "abc", t = "bcd", k = 10)
    a.canConvertString(s = "aab", t = "bbb", k = 27)
    a.canConvertString("atmtxzjkz", "tvbtjhvjd", 35)