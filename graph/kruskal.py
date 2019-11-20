# -*- coding: utf-8 -*-
# ======================================
# @File    : kruskal.py
# @Time    : 2019/11/19 22:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from graph.graph_utils import *
from graph.union_find import WeightedQuickUnionUF
import heapq

# Kruskal算法求最小生成树
def kruskal(n, graph):
    # 加权quick-union
    uf = WeightedQuickUnionUF(n)
    pq = []
    res = []
    for u in range(n):
        e = graph[u]
        while e:
            heapq.heappush(pq, e)
            e = e.next
    while pq and len(res) < n - 1:
        e = heapq.heappop(pq)
        u, v = e.u, e.v
        # 忽略失效边
        if uf.connected(u, v): continue
        # 添加新边时将边两端的节点连通
        uf.union(u, v)
        res.append(e)
    for e in res:
        print("%d -[%.2f]- %d" % (e.u, e.w, e.v))


if __name__ == '__main__':
    graph = build_graph(8, [[4, 5, .35], [4, 7, .37], [5, 7, .28], [0, 7, .16], [1, 5, .32], [0, 4, .38], [2, 3, .17],
                            [1, 7, .19], [0, 2, .26], [1, 2, .36], [1, 3, .29], [2, 7, .34], [6, 2, .40], [3, 6, .52],
                            [6, 0, .58], [6, 4, .93]],
                        direction=0, tp=2)
    kruskal(8, graph)