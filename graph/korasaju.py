# -*- coding: utf-8 -*-
# ======================================
# @File    : korasaju.py
# @Time    : 2019/11/18 23:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from graph.graph_utils import *

# korasaju算法（求强连通分量）

def reverse_post_dfs(n, graph):
    r_post = []
    marked = [0] * n
    def dfs(u):
        marked[u] = 1
        for v in graph[u]:
            if marked[v] == 0:
                dfs(v)
        r_post.append(u)
    for u in range(n):
        if marked[u] == 0:
            dfs(u)
    return r_post


def kosaraju(n, graph):
    r_graph = reverse_graph(graph)
    r_post = reverse_post_dfs(n, r_graph)
    print(r_post[::-1])
    ctr = 0
    color = [0] * n
    marked = [0] * n
    def dfs(u):
        nonlocal ctr
        marked[u] = 1
        color[u] = ctr
        for v in graph[u]:
            if not marked[v]:
                dfs(v)
    for u in r_post[::-1]:
        if not marked[u]:
            dfs(u)
            ctr += 1
    return color, ctr


def strongly_connected(n, connections):
    graph = build_graph(connections)
    color, ctr = kosaraju(n, graph)
    print(ctr)
    print(color)
    return color, ctr


if __name__ == '__main__':
    # strongly_connected(10, [[0,1],[1,2],[2,3],[2,4],[4,3],[4,5],[5,2],[4,6],[6,7],[7,1],[7,8],[8,9]])
    strongly_connected(13, [[0,1],[0,5],[2,0],[2,3],[3,2],[3,5],[4,2],[4,3],[5,4],[6,0],[6,4],[6,9],[7,6],[7,8],[8,7],[8,9],[9,10],[9,11],[10,12],[11,4],[11,12],[12,9]])


