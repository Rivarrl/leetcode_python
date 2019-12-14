# -*- coding: utf-8 -*-
# ======================================
# @File    : 5127.py
# @Time    : 2019/12/14 22:45
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        last = 0
        for i, j in sorted(intervals):
            if last >= j:
                n -= 1
            else:
                last = j
        return n


if __name__ == '__main__':
    a = Solution()
    a.removeCoveredIntervals([[1,4],[3,6],[2,8]])
