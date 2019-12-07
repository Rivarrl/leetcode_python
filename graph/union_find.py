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
        # 小树加入大树
        if self.sz[i] < self.sz[j]:
            self.idx[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.idx[j] = i
            self.sz[i] += self.sz[j]
        self.ctr -= 1

# 路径压缩版(递归)
# 路径表示父子关系，但是我们只想知道哪些点是连通的，也就是哪些点是一族的。
# 表示父子关系的结构比表示族群关系的结构信息量要大，自然查找深度就大
# 路径压缩就是破坏父子关系的表示，让所有同族节点直接指向自己族的代表（祖先），祖先节点指自己
class PathZippedQuickUnionUF(UF):
    def __init__(self, n):
        super().__init__(n)

    def find(self, p):
        if p == self.idx[p]:
            return p
        else:
            self.idx[p] = self.find(self.idx[p])
            return self.idx[p]

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j: return
        self.idx[j] = i

# 路径压缩+加权版(非递归)
# 非递归压缩的没有递归的狠
# 它的一次union操作只是把途经的节点去指自己祖父节点，并不能像递归版那样把途经的所有节点都只指向祖先节点
class PathZippedWeightedQuickUnionUF(UF):
    def __init__(self, n):
        super().__init__(n)
        self.sz = [1] * n

    def find(self, p):
        while p != self.idx[p]:
            self.idx[p] = self.idx[self.idx[p]]
            p = self.idx[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j: return
        if self.sz[i] > self.sz[j]:
            self.idx[j] = i
            self.sz[i] += self.sz[j]
        else:
            self.idx[i] = j
            self.sz[j] += self.sz[i]
