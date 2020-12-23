# -*- coding: utf-8 -*-
# ======================================
# @File    : 684.py
# @Time    : 2020/12/23 9:40 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [684. 冗余连接](https://leetcode-cn.com/problems/redundant-connection/)
    """
    @timeit
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 并查集
        n = len(edges)
        dsu = [i for i in range(n+1)]
        def find(u):
            if u == dsu[u]: return u
            dsu[u] = find(dsu[u])
            return dsu[u]
        def union(u, v):
            x, y = find(u), find(v)
            if x == y: return False
            dsu[x] = y
            return True
        for x in edges:
            if not union(*x):
                return x
        return [-1, -1]

if __name__ == '__main__':
    a = Solution()
    a.findRedundantConnection([[1,2], [1,3], [2,3]])
    a.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])