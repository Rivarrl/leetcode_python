# -*- coding: utf-8 -*-
# ======================================
# @File    : 1599.py
# @Time    : 2020/10/1 12:14
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1599. 经营摩天轮的最大利润](https://leetcode-cn.com/problems/maximum-profit-of-operating-a-centennial-wheel/)
    """
    @timeit
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost: return -1
        r = 0
        last = 0
        n = len(customers)
        for i in range(n):
            


if __name__ == '__main__':
    a = Solution()
    a.minOperationsMaxProfit(customers = [8,3], boardingCost = 5, runningCost = 6)
    a.minOperationsMaxProfit(customers = [10,9,6], boardingCost = 6, runningCost = 4)
    a.minOperationsMaxProfit(customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92)
    a.minOperationsMaxProfit(customers = [10,10,6,4,7], boardingCost = 3, runningCost = 8)