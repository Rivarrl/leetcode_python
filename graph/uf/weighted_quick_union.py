# -*- coding: utf-8 -*-
# ======================================
# @File    : weighted_quick_union.py
# @Time    : 2019/11/20 17:35
# @Author  : Rivarrl
# ======================================
from collections import defaultdict
from graph.uf.union_find import UF

# Union-Find（并查集）
# weighted-quick-union

class WeightedQuickUnionUF(UF):
    def __init__(self, n):
        super().__init__(n)
        # 存储以p为根节点的分量大小
        self.sz = [1] * n

    def find(self, p):
        while self.idx[p] != p:
            p = self.idx[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j: return
        if self.sz[i] < self.sz[j]:
            self.idx[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.idx[j] = i
            self.sz[i] += self.sz[j]
        self.ctr -= 1