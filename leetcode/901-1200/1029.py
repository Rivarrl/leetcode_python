# -*- coding: utf-8 -*-
# ======================================
# @File    : 1029.py
# @Time    : 2020/5/9 0:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1029. 两地调度](https://leetcode-cn.com/problems/two-city-scheduling/)
    """
    @timeit
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        n = len(costs) // 2
        res = 0
        for i in range(n):
            j = i + n
            res += costs[i][0] + costs[j][1]
        return res

if __name__ == '__main__':
    a = Solution()
    a.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])