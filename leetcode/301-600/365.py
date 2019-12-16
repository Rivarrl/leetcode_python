# -*- coding: utf-8 -*-
# ======================================
# @File    : 365.py
# @Time    : 2019/12/16 14:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [365. 水壶问题](https://leetcode-cn.com/problems/water-and-jug-problem/)
    """
    @timeit
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(x, y):
            if x == 0: return y
            return gcd(y%x, x)
        if x == 0 and y == 0: return z == 0
        if x + y < z: return False
        a = gcd(x, y)
        if a == 0: return False
        return z % a == 0

if __name__ == '__main__':
    a = Solution()
    a.canMeasureWater(1,1,3)
    a.canMeasureWater(3, 5, 4)
    a.canMeasureWater(2, 6, 5)