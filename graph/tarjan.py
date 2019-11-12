# -*- coding: utf-8 -*-
# ======================================
# @File    : tarjan.py
# @Time    : 2019/11/12 23:16
# @Author  : Rivarrl
# ======================================

def strongly_connected(n, connections):
    from collections import defaultdict
    # 构图，邻接表
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)

    # tarjan所需的数据结构
    stk, dfn, low, vis, color = [], [-1] * n, [-1] * n, [0] * n, [0] * n
    timestamp, idx = 0, 0

    def tarjan(u):
        nonlocal timestamp
        # 加时间戳
        dfn[u] = low[u] = timestamp
        timestamp += 1
        # 当前节点入栈
        stk.append(u)
        vis[u] = 1
        for v in graph[u]:
            # 访问未被访问的节点
            if dfn[v] < 0:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif vis[v]:  # 还在栈中，说明是返祖边或者符合同一强连通分量的横叉边
                low[u] = min(low[u], dfn[v])
        # dfn == low 说明是强连通分量的根
        if dfn[u] == low[u]:
            nonlocal idx
            idx += 1
            while u != stk[-1]:
                v = stk.pop()
                # 出栈恢复vis
                vis[v] = 0
                # 为同一强连通分量内的节点涂上相同的颜色
                color[v] = idx
    tarjan(0)

if __name__ == '__main__':
    strongly_connected(5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]])