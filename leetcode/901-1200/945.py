# -*- coding: utf-8 -*-
# ======================================
# @File    : 945.py
# @Time    : 2020/3/22 8:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minIncrementForUnique(self, A: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        m = 0
        for a in A:
            d[a] = d.get(a, 0) + 1
            m = max(m, a)
        res = 0
        for i in range(80001):
            if d[i] <= 1: continue
            d[i + 1] += d[i] - 1
            res += d[i] - 1
            d[i] = 1
        return res

    @timeit
    def minIncrementForUnique2(self, A: List[int]) -> int:
        A.sort()
        A += [100000]
        res = inc = 0
        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                inc += 1
                res -= A[i]
            else:
                t = min(inc, A[i] - A[i-1] - 1)
                res += A[i-1] * t + (1 + t) * t // 2
                inc -= t
        return res

if __name__ == '__main__':
    a = Solution()
    a.minIncrementForUnique2([1,2,2])
    a.minIncrementForUnique2([3,2,1,2,1,7])