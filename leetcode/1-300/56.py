# -*- coding: utf-8 -*-
# ======================================
# @File    : 56.py
# @Time    : 2020/4/16 0:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for left, right in intervals:
            if not res or res[-1][1] < left:
                res.append([left, right])
            else:
                res[-1][1] = max(res[-1][1], right)
        return res


if __name__ == '__main__':
    a = Solution()
    a.merge([[1,3],[2,6],[8,10],[15,18]])
    a.merge([[1,4],[4,5]])