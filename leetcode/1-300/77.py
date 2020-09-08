# -*- coding: utf-8 -*-
# ======================================
# @File    : 77.py
# @Time    : 2020/9/8 9:50 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [77. 组合](https://leetcode-cn.com/problems/combinations/)
    """
    @timeit
    def combine(self, n: int, k: int) -> List[List[int]]:
        def f(i, x):
            if n - i + 1 + len(x) < k: return
            if len(x) == k:
                res.append(x[:])
                return
            for j in range(i+1, n+1):
                x.append(j)
                f(j, x)
                x.pop()
        res = []
        f(0, [])
        return res

    @timeit
    def combine2(self, n: int, k: int) -> List[List[int]]:
        from functools import lru_cache
        @lru_cache(None)
        def f(m, n):
            if m == n: return [[e for e in range(1, n+1)]]
            if m == 1: return [[e] for e in range(1, n+1)]
            res = f(m, n-1)
            for x in f(m-1, n-1):
                res.append(x+[n])
            return res
        return f(k, n)

if __name__ == '__main__':
    a = Solution()
    r = a.combine2(4, 2)
