# -*- coding: utf-8 -*-
# ======================================
# @File    : 956.py
# @Time    : 2020/6/24 1:10 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [956. 最高的广告牌](https://leetcode-cn.com/problems/tallest-billboard/)
    """
    @timeit
    def tallestBillboard(self, rods: List[int]) -> int:
        from functools import lru_cache
        n = len(rods)
        rods.sort()
        inf = 0x3f3f3f3f
        suf = [0]
        for x in rods[::-1]:
            suf = [x+suf[0]] + suf
        @lru_cache(None)
        def f(i, k):
            if i == n:
                return 0 if k == 0 else -inf
            if abs(k) > suf[i]: return -inf
            return max(f(i+1, k), f(i+1, k+rods[i]), f(i+1, k-rods[i]) + rods[i])
        return f(0, 0)

if __name__ == '__main__':
    a = Solution()
    a.tallestBillboard([1,2,3,6])
    a.tallestBillboard([1,2,3,4,5,6])
    a.tallestBillboard([1,2])