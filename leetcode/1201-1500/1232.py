# -*- coding: utf-8 -*-
# ======================================
# @File    : 1232.py
# @Time    : 2021/1/17 22:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1232. 缀点成线](https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/)
    """
    @timeit
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2: return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        k = (y2-y1) / (x2-x1) if x1 != x2 else float('inf')
        for i in range(2, n):
            x1, y1, x2, y2 = x2, y2, coordinates[i][0], coordinates[i][1]
            k1 = (y2 - y1) / (x2 - x1) if x1 != x2 else float('inf')
            if k != k1: return False
        return True

if __name__ == '__main__':
    a = Solution()
    a.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])
    a.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])
