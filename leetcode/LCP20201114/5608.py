# -*- coding: utf-8 -*-
# ======================================
# @File    : 5608.py
# @Time    : 2020/11/22 11:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:(x[1]-x[0], x[1], x[0]))
        res = tasks[0][1] - tasks[0][0]
        for x, y in tasks:
            if res + x >= y:
                res += x
            else:
                res = y
        return res

if __name__ == '__main__':
    a = Solution()
    a.minimumEffort(tasks = [[1,2],[2,4],[4,8]])
    a.minimumEffort(tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]])
    a.minimumEffort(tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]])