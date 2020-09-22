# -*- coding: utf-8 -*-
# ======================================
# @File    : 7.py
# @Time    : 2020/9/19 15:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def paintingPlan(self, n: int, k: int) -> int:
        if k == 0 or k == n*n: return 1
        if k < n: return 0
        fab = [1, 1, 2, 6, 24, 120, 720]
        def f(x): return fab[n] // (fab[x]*fab[n-x])
        res = 0
        for r in range(n+1):
            for c in range(n+1):
                x = n*(r+c) - (r*c)
                if x == k:
                    print(r, c)
                    res += f(r) * f(c)
        return res

if __name__ == '__main__':
    a = Solution()
    # a.paintingPlan(n = 2, k = 2)
    # a.paintingPlan(n = 2, k = 1)
    a.paintingPlan(n = 2, k = 4)