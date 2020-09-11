# -*- coding: utf-8 -*-
# ======================================
# @File    : 216.py
# @Time    : 2020/9/11 1:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [216. 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/)
    """
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

    @timeit
    def combinationSum32(self, k: int, n: int) -> List[List[int]]:
        if k > 9 or k < 1: return []
        if n > 45 or n < 1: return []
        def bit_count(mask):
            res = 0
            while mask:
                mask &= (mask - 1)
                res += 1
            return res
        res = []
        for mask in range(1 << 9):
            if bit_count(mask) == k:
                cur = sum([i+1 for i in range(9) if mask & (1 << i)])
                if cur == n:
                    res.append([i+1 for i in range(9) if mask & (1 << i)])
        return res

if __name__ == '__main__':
    a = Solution()
    a.combinationSum3(3, 7)
    a.combinationSum3(3, 9)
    a.combinationSum32(3, 7)
    a.combinationSum32(3, 9)