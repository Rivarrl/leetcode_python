# -*- coding: utf-8 -*-
# ======================================
# @File    : 216.py
# @Time    : 2020/9/11 1:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > 9 or k < 1: return []
        if n > 45 or n < 1: return []
        def f(j, n, k):
            if n < k: return []
            res = []
            if k == 1 and 0 < n < 10:
                res.append([n])
            for i in range(j, min(10, n+1)):
                for x in f(i + 1, n - i, k - 1):
                    sx = sorted([i] + x)
                    if not i in x and not sx in res:
                        res.append(sx)
            return res
        return f(1, n, k)

if __name__ == '__main__':
    a = Solution()
    a.combinationSum3(3, 7)
    a.combinationSum3(3, 9)