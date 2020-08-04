# -*- coding: utf-8 -*-
# ======================================
# @File    : 1465.py
# @Time    : 2020/6/1 18:23
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1465. 切割后面积最大的蛋糕](https://leetcode-cn.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)
    """
    @timeit
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hor = [0] + sorted(horizontalCuts) + [h]
        ver = [0] + sorted(verticalCuts) + [w]
        m = n = 0
        for i in range(len(hor)-1):
            m = max(m,  hor[i+1] - hor[i])
        for i in range(len(ver)-1):
            n = max(n,  ver[i+1] - ver[i])
        return (n * m) % (10 ** 9 + 7)

if __name__ == '__main__':
    a = Solution()
    a.maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3])
    a.maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1])
    a.maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3])