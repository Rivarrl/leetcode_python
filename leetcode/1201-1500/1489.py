# -*- coding: utf-8 -*-
# ======================================
# @File    : 1489.py
# @Time    : 2020/6/28 2:41 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class UnionFind:
    def __init__(self, n):
        self.dsu = list(range(n))
        self.sz = [1] * n



class Solution:
    @timeit
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i, x in enumerate(edges):
            x.append(i)
        edges.sort(key=lambda x:x[-1])
        dsu = list(range(n))
        


if __name__ == '__main__':
    a = Solution()
    a.findCriticalAndPseudoCriticalEdges()
    a.findCriticalAndPseudoCriticalEdges()