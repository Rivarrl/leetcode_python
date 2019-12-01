# -*- coding: utf-8 -*-
# ======================================
# @File    : 5276.py
# @Time    : 2019/12/1 10:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    5276. 不浪费原料的汉堡制作方案
    # 比赛的时候懵逼了，用的二分查找
    # 解方程就可以
    """
    @timeit
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        def tomato(x, y): return 4 * x + 2 * y
        lo, hi = 0, cheeseSlices
        while lo <= hi:
            x = (lo + hi + 1) // 2
            y = cheeseSlices - x
            tmt = tomato(x, y)
            if tmt == tomatoSlices:
                return [x, y]
            elif tmt > tomatoSlices:
                hi = x - 1
            else:
                lo = x + 1
        return []

    @timeit
    def numOfBurgers2(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 解方程版
        a = 4 * cheeseSlices - tomatoSlices
        if a < 0 or a > 2 * cheeseSlices or a & 1: return []
        y = a // 2
        return [cheeseSlices - y, y]


if __name__ == '__main__':
    a = Solution()
    a.numOfBurgers2(16,7)
    a.numOfBurgers2(17,4)
    a.numOfBurgers2(4,17)
    a.numOfBurgers2(0,0)
    a.numOfBurgers2(2,1)
    a.numOfBurgers2(2926962,2144628)
