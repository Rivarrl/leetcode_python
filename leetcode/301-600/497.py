# -*- coding: utf-8 -*-
# ======================================
# @File    : 497.py
# @Time    : 2020/5/11 23:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

import random
class Solution:
    """
    [497. 非重叠矩形中的随机点](https://leetcode-cn.com/problems/random-point-in-non-overlapping-rectangles/)
    """
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.tot = 0
        self.arr = []
        for x in rects:
            self.tot += (x[2] - x[0] + 1) * (x[3] - x[1] + 1)
            self.arr.append(self.tot)

    def pick(self) -> List[int]:
        rd = random.randint(0, self.tot-1)
        lo, hi = 0, len(self.rects) - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if rd >= self.arr[mi]:
                lo = mi + 1
            else:
                hi = mi
        x = self.rects[lo]
        width, height = x[2] - x[0] + 1, x[3] - x[1] + 1
        base = self.arr[lo] - width * height
        return [x[0] + (rd - base) % width, x[1] + (rd - base) // width]

if __name__ == '__main__':
    a = Solution([[1,1,5,5]])
    a.pick()
    a.pick()
    a.pick()
    a = Solution([[-2,-2,-1,-1],[1,0,3,0]])
    a.pick()
    a.pick()
    a.pick()
    a.pick()
    a.pick()