# -*- coding: utf-8 -*-
# ======================================
# @File    : 836.py
# @Time    : 2020/3/18 0:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        X = sorted([rec1[0], rec1[2], rec2[0], rec2[2]])
        Y = sorted([rec1[1], rec1[3], rec2[1], rec2[3]])
        if X[-1] - X[0] < rec1[2] - rec1[0] + rec2[2] - rec2[0] \
                and Y[-1] - Y[0] < rec1[3] - rec1[1] + rec2[3] - rec2[1]:
            return True
        return False

    def isRectangleOverlap2(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return (x4-x1)*(x3-x2) < 0 and (y4-y1)*(y3-y2) < 0



if __name__ == '__main__':
    a = Solution()
    a.isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3])
    a.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1])
    a.isRectangleOverlap([7,8,13,15], [10,8,12,20])