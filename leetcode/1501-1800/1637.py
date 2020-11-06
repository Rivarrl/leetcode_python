# -*- coding: utf-8 -*-
# ======================================
# @File    : 1637.py
# @Time    : 2020/11/6 12:55 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1637. 两点之间不包含任何点的最宽垂直面积]()
    """
    @timeit
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = sorted([e[0] for e in points])
        n = len(arr)
        res = 0
        for i in range(1, n):
            res = max(res, arr[i] - arr[i-1])
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]])
    a.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])