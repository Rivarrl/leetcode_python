# -*- coding: utf-8 -*-
# ======================================
# @File    : quick_union.py
# @Time    : 2019/11/20 17:34
# @Author  : Rivarrl
# ======================================
from collections import defaultdict
from graph.uf.union_find import UF

# Union-Find（并查集）
# quick-union的实现


class QuickUnionUF(UF):
    def __init__(self, n):
        super().__init__(n)
    
    def find(self, p):
        while self.idx[p] != p:
            p = self.idx[p]
        return p
    
    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j: return
        self.idx[i] = j
        self.ctr -= 1
