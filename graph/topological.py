# -*- coding: utf-8 -*-
# ======================================
# @File    : topological.py
# @Time    : 2019/11/21 21:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from graph.graph_utils import *

# 有向无环图的拓扑排序

def topological(n, graph):
    degree_in = [0] * n
    for u in range(n):
        for v in graph[u]:
            degree_in[v] += 1
    stk = [u for u in range(n) if degree_in[u] == 0]
    res = []
    while stk:
        u = stk.pop()
        res.append(u)
        for v in graph[u]:
            degree_in[v] -= 1
            if degree_in[v] == 0:
                stk.insert(0, v)
    return res


if __name__ == '__main__':
    graph = build_graph(8, [[0,1],[1,2],[1,3],[2,5],[5,6],[3,6],[6,4],[4,7],[6,7]])
    res = topological(8, graph)
    print(res)