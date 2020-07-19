# -*- coding: utf-8 -*-
# ======================================
# @File    : 312.py
# @Time    : 2020/7/19 15:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def maxCoins(self, nums: List[int]) -> int:
        from functools import lru_cache
        n = len(nums)
        val = [1] + nums + [1]
        @lru_cache(None)
        def f(l, r):
            if l >= r - 1: return 0
            best = 0
            for i in range(l+1, r):
                total = val[l] * val[i] * val[r]
                total += f(l, i) + f(i, r)
                best = max(best, total)
            return best
        return f(0, n + 1)

if __name__ == '__main__':
    a = Solution()
    a.maxCoins([3,1,5,8])