# -*- coding: utf-8 -*-
# ======================================
# @File    : 435.py
# @Time    : 2020/11/25 10:12 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)
    """
    @timeit
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], x[0]))
        stk = []
        for x, y in intervals:
            if not stk or stk[-1][1] <= x:
                stk.append([x, y])
        return len(intervals) - len(stk)


if __name__ == '__main__':
    a = Solution()
    a.eraseOverlapIntervals([[1,2], [2,3], [3,4], [1,3]])
    a.eraseOverlapIntervals([[1,2], [1,2], [1,2]])
    a.eraseOverlapIntervals([[1,2], [2,3]])