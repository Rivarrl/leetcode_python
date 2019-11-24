# -*- coding: utf-8 -*-
# ======================================
# @File    : 5271.py
# @Time    : 2019/11/24 10:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
class Solution:
    """
    5271. 访问所有点的最小时间
    """
    @timeit
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x, y = points[0]
        if len(points) == 1: return 0
        res = 0
        for i, j in points[1:]:
            res += max(abs(i - x), abs(j - y))
            x, y = i, j
        return res




if __name__ == '__main__':
    a = Solution()
    a.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
    a.minTimeToVisitAllPoints([[3,2],[-2,2]])
