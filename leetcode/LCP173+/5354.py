# -*- coding: utf-8 -*-
# ======================================
# @File    : 5354.py
# @Time    : 2020/3/8 10:52
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        from collections import defaultdict
        g = defaultdict(list)
        for i in range(n):
            if manager[i] >= 0:
                g[manager[i]].append(i)
        stk = [(headID, 0)]
        res = 0
        while stk:
            i, m = stk.pop(0)
            res = max(res, m)
            for j in g[i]:
                stk.append((j, m + informTime[i]))
        return res


if __name__ == '__main__':
    a = Solution()
    a.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0])
    a.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0])
    a.numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1])
    a.numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
    a.numOfMinutes(n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914])
