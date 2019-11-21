# -*- coding: utf-8 -*-
# ======================================
# @File    : acyclicsp.py
# @Time    : 2019/11/21 21:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from graph.graph_utils import *

def topological(n, graph):
    degree_in = [0] * n
    for u in range(n):
        e = graph[u]
        while e:
            degree_in[e.v] += 1
            e = e.next
    stk = [u for u in range(n) if degree_in[u] == 0]
    res = []
    while stk:
        u = stk.pop()
        res.append(u)
        e = graph[u]
        while e:
            v = e.v
            degree_in[v] -= 1
            if degree_in[v] == 0:
                stk.append(v)
            e = e.next
    return res

# 有向无环图的拓扑排序求最短路径方法
def acyclic_sp(n, graph, s):
    tp = topological(n, graph)
    dist_to = [inf_w] * n
    edge_to = [None] * n
    dist_to[s] = 0.0
    def relax(u):
        e = graph[u]
        while e:
            v, w = e.v, e.w
            if dist_to[v] > dist_to[u] + w:
                dist_to[v] = dist_to[u] + w
                edge_to[v] = e
            e = e.next
    for u in tp:
        relax(u)
    display(n, s, dist_to, edge_to)

def display(n, s, dist_to, edge_to):
    paths = [list() for _ in range(n)]
    for v in range(n):
        if v != s and dist_to[v] != inf_w:
            e = edge_to[v]
            while e:
                paths[v].append(e)
                e = edge_to[e.u]
    for i, path in enumerate(paths):
        if not path:
            print(i, "/")
            continue
        print(i, end=' ')
        for j in range(len(path)-1, -1, -1):
            e = path[j]
            if j == 0:
                print("%d -[%.2f]-> %d" % (e.u, e.w, e.v))
            else:
                print("%d -[%.2f]-> " % (e.u, e.w), end='')


if __name__ == '__main__':
    graph = build_graph(8, [[0,1,0.33],[1,2,0.23],[1,3,0.55],[2,5,0.77],
                            [5,6,1.01],[3,6,1.45],[6,4,0.68],[4,7,2.10],[6,7,0.65]],
                        direction=1, tp=2)
    acyclic_sp(8, graph, 0)