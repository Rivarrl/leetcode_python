# -*- coding: utf-8 -*-
# ======================================
# @File    : 902.py
# @Time    : 2019/11/22 1:13
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [902. 最大为 N 的数字组合](https://leetcode-cn.com/problems/numbers-at-most-n-given-digit-set/)
    """
    @timeit
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        """
        思路：动态规划，假设给定的N有x位，那么x-1位的值可以直接计算得到，n+n^2+..+n^(x-1)
        """
        def f(x, y):
            res = 0
            for i in range(1, y+1):
                res += x ** i
            return res
        def t(D, x):
            for i in range(len(D)):
                if D[i] > x: return i
            return len(D)
        def p(base, l):
            for x in range(l):
                base *= n
            return base
        def g(i):
            if i == digit - 1: return t(D, sn[i])
            r = 0
            while r < n and D[r] < sn[i]:
                r += 1
            if r < n and D[r] == sn[i]:
                if r == 0: return g(i+1)
                else: return p(r, digit-1-i) + g(i+1)
            else:
                return p(r, digit-1-i)

        digit = len(str(N))
        n = len(D)
        res = 0
        res += f(n, digit - 1)
        sn = str(N)
        res += g(0)
        return res


if __name__ == '__main__':
    a = Solution()
    # a.atMostNGivenDigitSet(["1","2","3"], 120)
    a.atMostNGivenDigitSet(["1","7"], 231)
    a.atMostNGivenDigitSet(["1"], 834)
    a.atMostNGivenDigitSet(["5","7","8"], 59)
