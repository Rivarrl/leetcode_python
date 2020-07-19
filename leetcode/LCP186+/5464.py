# -*- coding: utf-8 -*-
# ======================================
# @File    : 5464.py
# @Time    : 2020/7/19 10:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5464. 换酒问题]()
    """
    @timeit
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = n = numBottles
        while n >= numExchange:
            x = n // numExchange
            n = n % numExchange + x
            res += x
        return res

if __name__ == '__main__':
    a = Solution()
    a.numWaterBottles(9, 3)
    a.numWaterBottles(15, 4)
    a.numWaterBottles(5,5)
    a.numWaterBottles(2,3)
