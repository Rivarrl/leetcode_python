# -*- coding: utf-8 -*-
# ======================================
# @File    : 5368.py
# @Time    : 2020/3/29 10:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        m = 0
        for e in arr:
            d[e] = d.get(e, 0) + 1
            m = max(m, d[e])
        for i in range(m+1, 0, -1):
            if d.get(i, 0) == i:
                return i
        return -1

if __name__ == '__main__':
    a = Solution()
    a.findLucky(arr = [2,2,3,4])
    a.findLucky(arr = [1,2,2,3,3,3])
    a.findLucky(arr = [2,2,2,3,3])
    a.findLucky([5])
    a.findLucky(arr = [7,7,7,7,7,7,7])