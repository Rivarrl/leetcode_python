# -*- coding: utf-8 -*-
# ======================================
# @File    : 5400.py
# @Time    : 2020/5/3 10:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5400. 旅行终点站]()
    """
    @timeit
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for u, v in paths:
            d[u] = d.get(u, 0) + 1
            d[v] = d.get(v, 0) - 1
        for k, v in d.items():
            if v == -1:
                return k

if __name__ == '__main__':
    a = Solution()
    a.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
    a.destCity(paths = [["B","C"],["D","B"],["C","A"]])
    a.destCity(paths = [["A","Z"]])