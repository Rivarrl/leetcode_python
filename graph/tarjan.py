# -*- coding: utf-8 -*-
# ======================================
# @File    : tarjan.py
# @Time    : 2019/11/12 23:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from graph.graph_utils import *

@timeit
def strongly_connected(n, connections):
    """
    找所有强连通分量，并染色
    """
    graph = build_graph(n, connections)
    # tarjan所需的数据结构
    stk, dfn, low, vis, color = [], [0] * n, [0] * n, [0] * n, [0] * n
    timestamp, idx = 0, 0

    def tarjan(u):
        nonlocal timestamp
        timestamp += 1
        # 加时间戳
        dfn[u] = low[u] = timestamp
        # 当前节点入栈
        stk.append(u)
        vis[u] = 1
        for v in graph[u]:
            # 访问未被访问的节点
            if not dfn[v]:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif vis[v]:  # 还在栈中，说明是返祖边或者符合同一强连通分量的横叉边
                low[u] = min(low[u], dfn[v])
        # dfn == low 说明是强连通分量的根
        if dfn[u] == low[u]:
            nonlocal idx
            idx += 1
            color[u] = idx
            vis[u] = 0
            while u != stk[-1]:
                v = stk.pop()
                # 出栈恢复vis
                vis[v] = 0
                # 为同一强连通分量内的节点涂上相同的颜色
                color[v] = idx
            stk.pop()
    for i in range(n):
        if not dfn[i]:
            tarjan(i)
    return color


@timeit
def find_cut_point(n, connections):
    """
    找割点，割点就是把这个点和它的边删除之后，图不再连通(连通分量数量增多)
    """
    graph = build_graph(n, connections)
    dfn, low = [0] * n, [0] * n
    # 割点
    cut = [0] * n
    timestamp = 0
    def tarjan(u, fa):
        nonlocal timestamp
        timestamp += 1
        # root_count，根的子节点计数
        rc = 0
        dfn[u] = low[u] = timestamp
        for v in graph[u]:
            # 未访问过
            if not dfn[v]:
                tarjan(v, fa)
                low[u] = min(low[u], low[v])
                # 非根节点的割点判断
                if low[v] >= dfn[u] and u != fa: cut[u] = 1
                if u == fa: rc += 1
            low[u] = min(low[u], dfn[v])
        # 根节点的割点判断
        if u == fa and rc >= 2: cut[u] = 1
    for i in range(n):
        if not dfn[i]:
            tarjan(i, i)
    res = []
    for i in range(n):
        if cut[i]:
            res.append(i)
    return res


@timeit
def find_bridge(n, connections):
    """
    找桥
    """
    graph = build_graph(n, connections)
    dfn, low, res = [0] * n, [0] * n, []
    timestamp = 0
    def tarjan(u, fa):
        nonlocal timestamp
        timestamp += 1
        dfn[u] = low[u] = timestamp
        for v in graph[u]:
            if not dfn[v]:
                tarjan(v, fa)
                low[u] = min(low[u], low[v])
                if low[v] > dfn[u]:
                    res.append([u, v])
            elif u != fa and dfn[v] < dfn[u]: # 指回更靠前的点
                low[u] = min(low[u], dfn[v])
    for i in range(n):
        if not dfn[i]:
            tarjan(i, i)
    return res


@timeit
def to_dag(n, connections):
    """
    缩点，前面几乎与强连通分量相同
    """
    graph = build_graph(n, connections)
    stk, dfn, low, vis, color = [], [0] * n, [0] * n, [0] * n, [0] * n
    timestamp, idx = 0, 0

    def tarjan(u):
        nonlocal timestamp
        timestamp += 1
        dfn[u] = low[u] = timestamp
        stk.append(u)
        vis[u] = 1
        for v in graph[u]:
            if not dfn[v]:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif vis[v]:
                low[u] = min(low[u], dfn[v])
        if dfn[u] == low[u]:
            nonlocal idx
            idx += 1
            color[u] = idx
            vis[u] = 0
            while u != stk[-1]:
                v = stk.pop()
                vis[v] = 0
                color[v] = idx
            stk.pop()

    for i in range(n):
        if not dfn[i]:
            tarjan(i)
    dag = defaultdict(list)
    for u in range(n):
        for v in graph[u]:
            if color[u] != color[v]:
                if color[v] in dag[color[u]]: continue
                dag[color[u]].append(color[v])
    return dag


if __name__ == '__main__':
    strongly_connected(10, [[0,1],[1,2],[2,3],[2,4],[4,3],[4,5],[5,2],[4,6],[6,7],[7,1],[7,8],[8,9]])
    # find_cut_point(11, [[0,1],[0,3],[0,4],[0,5],[1,10],[1,2],[3,2],[3,8],[4,7],[4,6],[5,6],[6,9],[10,2]])
    # find_bridge(11, [[0,1],[0,3],[0,4],[0,5],[1,10],[1,2],[3,2],[3,8],[4,7],[4,6],[5,6],[6,9],[10,2]])
    # to_dag(10, [[0,1],[1,2],[2,3],[2,4],[4,3],[4,5],[5,2],[4,6],[6,7],[7,1],[7,8],[8,9]])
