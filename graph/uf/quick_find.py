# -*- coding: utf-8 -*-
# ======================================
# @File    : quick_find.py
# @Time    : 2019/11/20 17:22
# @Author  : Rivarrl
# ======================================
from collections import defaultdict
from graph.uf.union_find import UF

# Union-Find（并查集）
# quick-find实现


class QuickFindUF(UF):
    def __init__(self, n):
        super().__init__(n)

    def find(self, p):
        return self.idx[p]

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j: return
        for k in range(len(self.idx)):
            if self.idx[k] == i:
                self.idx[k] = j
        self.ctr -= 1