# -*- coding: utf-8 -*-
# ======================================
# @File    : P3387.py
# @Time    : 2019/11/14 19:28
# @Author  : Rivarrl
# ======================================

import sys
sys.setrecursionlimit(10010)

def tarjan(u):
    global timestamp, col_id
    timestamp += 1
    dfn[u] = low[u] = timestamp
    stk.append(u)
    vis[u] = 1
    for v in graph[u]:
        if not dfn[v]:
            tarjan(v)
            low[u] = min(low[u], low[v])
        elif vis[u]:
            low[u] = min(low[u], dfn[v])
    if low[u] == dfn[u]:
        color[u] = col_id
        vis[u] = 0
        while u != stk[-1]:
            v = stk.pop()
            color[v] = col_id
            vis[v] = 0
        stk.pop()
        col_id += 1


# 【模板】缩点
if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    n, m = list(map(int, line1.split(' ')))
    graph = [[] for _ in range(n+1)]
    dfn, low, stk, vis, color = [0] * (n+1), [0] * (n+1), [], [0] * (n+1), [0] * (n+1)
    timestamp, col_id = 0, 0
    line2 = sys.stdin.readline().strip()
    w = list(map(int, line2.split(' ')))
    w = [0] + w
    for i in range(m):
        line = sys.stdin.readline().strip()
        fr, to = list(map(int, line.split(' ')))
        graph[fr].append(to)
    for i in range(n):
        if not dfn[i+1]:
            tarjan(i+1)
    dag = [[]] * col_id
    dagw = [0] * col_id

    for u in range(1, n+1):
        dagw[color[u]] += w[u]

    for u in range(1, n+1):
        for v in graph[u]:
            if color[v] != color[u] and color[v] not in dag[color[u]]:
                dag[color[u]].append(color[v])
