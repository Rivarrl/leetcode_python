# -*- coding: utf-8 -*-
# ======================================
# @File    : 5622.py
# @Time    : 2020/12/26 22:42
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5622. 平均等待时间]()
    """
    @timeit
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        st, tt = customers[0]
        res = tt
        st += tt
        for arrival, t in customers[1:]:
            st = max(st, arrival) + t
            res += st - arrival
        return res / len(customers)

if __name__ == '__main__':
    a = Solution()
    a.averageWaitingTime(customers = [[1,2],[2,5],[4,3]])
    a.averageWaitingTime(customers = [[5,2],[5,4],[10,3],[20,1]])