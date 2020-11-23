# -*- coding: utf-8 -*-
# ======================================
# @File    : 452.py
# @Time    : 2020/11/23 9:43 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [452. 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)
    """
    @timeit
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res, cur = 0, None
        for l, r in points:
            if not cur or l > cur:
                cur = r
                res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]])
    a.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]])
    a.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]])
    a.findMinArrowShots(points = [[1,2]])
    a.findMinArrowShots(points = [[2,3],[2,3]])