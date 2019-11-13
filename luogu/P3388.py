# -*- coding: utf-8 -*-
# ======================================
# @File    : P3388.py
# @Time    : 2019/11/13 22:48
# @Author  : Rivarrl
# ======================================
import sys
# 递归默认层数998，一共最多10000个点，设成10010没问题了
sys.setrecursionlimit(10010)
# 模板题，割点
def tarjan(u, fa):
    global timestamp
    timestamp += 1
    dfn[u] = low[u] = timestamp
    rc = 0
    for v in graph[u]:
        if not dfn[v]:
            tarjan(v, u)
            low[u] = min(low[u], low[v])
            if u == fa: rc += 1
            if u != fa and low[v] >= dfn[u]: cut[u] = True
        elif v != fa:
            low[u] = min(low[u], dfn[v])
    if u == fa and rc >= 2: cut[u] = True


if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    n, m = list(map(int, line1.split(' ')))
    graph = [[] for _ in range(n+1)]
    ctr, res = 0, []
    timestamp = 0
    for _ in range(m):
        line = sys.stdin.readline().strip()
        a, b = list(map(int, line.split(' ')))
        graph[a].append(b)
        graph[b].append(a)
    dfn, low, cut = [0] * (n + 1), [0] * (n + 1), [False] * (n+1)
    for i in range(1, n+1):
        if not dfn[i]:
            tarjan(i, i)
    for i in range(1, n+1):
        if cut[i]:
            ctr += 1
            res.append(i)
    print(ctr)
    print(' '.join([str(e) for e in res]))

