# -*- coding: utf-8 -*-
# ======================================
# @File    : dijkstra_mindis.py
# @Time    : 2019/11/21 9:51
# @Author  : Rivarrl
# ======================================
from graph.graph_utils import *
import heapq

# Dijkstra单源最短路径算法

def dijkstra(n, graph, s):
    def relax(u):
        e = graph[u]
        while e:
            v = e.v
            if dist_to[v] > dist_to[u] + e.w:
                dist_to[v] = dist_to[u] + e.w
                edge_to[v] = e
                for i in range(len(pq)):
                    if pq[i][1] == v:
                        pq[i] = (dist_to[v], v)
                        heapq.heapify(pq)
                        break
                else:
                    heapq.heappush(pq, (dist_to[v], v))
            e = e.next
    edge_to = [None] * n
    dist_to = [inf_w] * n
    dist_to[s] = 0
    pq = []
    heapq.heappush(pq, (0.0, s))
    while pq:
        w, u = heapq.heappop(pq)
        relax(u)
    i = 0
    for e in edge_to:
        i += 1
        if not e:
            print(i)
            continue
        print("%d -[%.2f]- %d" % (e.u, e.w, e.v))


if __name__ == '__main__':
    graph = build_graph(8, [[4,5,.35],[4,7,.37],[5,7,.28],[0,7,.16],[1,5,.32],[0,4,.38],[2,3,.17],
                            [1,7,.19],[0,2,.26],[1,2,.36],[1,3,.29],[2,7,.34],[6,2,.40],[3,6,.52],
                            [6,0,.58],[6,4,.93]],
                direction=1, tp=2)
    dijkstra(8, graph, 0)