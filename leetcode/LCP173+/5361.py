# -*- coding: utf-8 -*-
# ======================================
# @File    : 5361.py
# @Time    : 2020/4/4 22:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5361. 圆和矩形是否有重叠](https://leetcode-cn.com/problems/circle-and-rectangle-overlapping/)
    """
    @timeit
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xb = (((x2 - x1) ** 2 + (y2-y1) ** 2)**0.5)*0.5
        dis = lambda x, y: ((x - x_center) ** 2 + (y-y_center)**2)**0.5
        x0, y0 = (x2+x1)/2, (y2+y1)/2
        xx = dis(x0, y0)
        if xx < xb + radius: return True
        elif xx > xb + radius: return False
        else:
            return any(dis(*e) == radius for e in ((x1, y1),(x1,y2),(x2,y1),(x2,y2)))

if __name__ == '__main__':
    a = Solution()
    a.checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1)
    a.checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1)
    a.checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3)
    a.checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1)