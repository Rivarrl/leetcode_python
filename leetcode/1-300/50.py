# -*- coding: utf-8 -*-
# ======================================
# @File    : 50.py
# @Time    : 2020/5/11 0:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            if n == 0: return 1
            return 0
        if n < 0:
            n = -n
            x = 1 / x
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.myPow(2.0000, 10)
    a.myPow(2.10000, 3)
    a.myPow(2.0000, -2)