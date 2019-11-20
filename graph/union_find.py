# -*- coding: utf-8 -*-
# ======================================
# @File    : union_find.py
# @Time    : 2019/11/20 17:37
# @Author  : Rivarrl
# ======================================

# Union-Find（并查集）
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