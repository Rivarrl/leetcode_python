# -*- coding: utf-8 -*-
# ======================================
# @File    : 121.py
# @Time    : 2020/3/9 0:07
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        tmp = 0x3f3f3f3f
        n = len(prices)
        for i in range(n):
            tmp = min(tmp, prices[i])
            res = max(res, prices[i] - tmp)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxProfit([7,1,5,3,6,4])
    a.maxProfit([7,6,4,3,1])