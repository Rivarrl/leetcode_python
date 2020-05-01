# -*- coding: utf-8 -*-
# ======================================
# @File    : 63.py
# @Time    : 2020/5/1 20:58
# @Author  : Rivarrl
# ======================================
# [面试题63. 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)

from algorithm_utils import *

class Solution:
    @timeit
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if not prices: return 0
        m = max(prices)
        for x in prices:
            res = max(res, x - m)
            m = min(m, x)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxProfit([7,1,5,3,6,4])
    a.maxProfit([7,6,4,3,1])