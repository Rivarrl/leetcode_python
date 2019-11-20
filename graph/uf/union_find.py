# -*- coding: utf-8 -*-
# ======================================
# @File    : union_find.py
# @Time    : 2019/11/20 17:37
# @Author  : Rivarrl
# ======================================

class UF:
    def __init__(self, n):
        # 触点连通的根节点编号
        self.idx = [i for i in range(n)]
        # 连通分量数
        self.ctr = n

    def count(self):
        return self.ctr

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        pass

    def union(self, p, q):
        pass
