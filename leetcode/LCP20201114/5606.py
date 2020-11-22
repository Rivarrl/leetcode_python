# -*- coding: utf-8 -*-
# ======================================
# @File    : 5606.py
# @Time    : 2020/11/22 10:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import sys
sys.setrecursionlimit(100000)

class Solution:
    @timeit
    def getSmallestString(self, n: int, k: int) -> str:
        alp = "abcdefghijklmnopqrstuvwxyz"
        res = ""
        while k // 26 + int(k % 26 > 0) < n:
            res += 'a'
            k -= 1
            n -= 1
        res += alp[(k-1) % 26] + "z" * (k // 26)
        return res


if __name__ == '__main__':
    a = Solution()
    a.getSmallestString(n = 3, k = 27)
    a.getSmallestString(n = 5, k = 73)
    a.getSmallestString(n=100000, k=2600000)