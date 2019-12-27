# -*- coding: utf-8 -*-
# ======================================
# @File    : 1037.py
# @Time    : 2019/12/26 0:17
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1037. 有效的回旋镖](https://leetcode-cn.com/problems/valid-boomerang/)
    """
    @timeit
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b, c = points
        if a == b or a == c or b == c: return False
        x1, x2 = a[0] - b[0], a[0] - c[0]
        if x1 == 0 or x2 == 0: return x1 == x2
        y1, y2 = a[1] - b[1], a[1] - c[1]
        k1, k2 = y1 / x1, y2 / x2
        return k1 != k2

if __name__ == '__main__':
    a = Solution()
    a.isBoomerang([[1,1],[2,3],[3,2]])
    a.isBoomerang([[1,1],[2,2],[3,3]])