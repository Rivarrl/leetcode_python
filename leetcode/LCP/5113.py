# -*- coding: utf-8 -*-
# ======================================
# @File    : 5113.py
# @Time    : 2019/11/30 22:38
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5113. 删除区间]
    """
    @timeit
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        x, y = toBeRemoved
        res = []
        n = len(intervals)
        for i in range(n):
            a, b = intervals[i]
            if b < x or a > y: res.append([a, b])
            elif a < x < y < b: res.extend([[a, x], [y, b]])
            elif a < x < b: res.append([a, x])
            elif a < y < b: res.append([y, b])
        return res


if __name__ == '__main__':
    a = Solution()
    a.removeInterval(intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6])
    a.removeInterval(intervals = [[0,5]], toBeRemoved = [2,3])
    a.removeInterval([[0,2],[3,6],[10,15]], [7,9])
    a.removeInterval([[0,2],[3,6],[10,15]], [5,9])