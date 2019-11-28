# -*- coding: utf-8 -*-
# ======================================
# @File    : P1129.py
# @Time    : 2019/11/28 17:20
# @Author  : Rivarrl
# ======================================
import sys

ans = ["No", "Yes"]
maxn = 201
cx, cy, vis = [-1] * maxn, [-1] * maxn, [0] * maxn
edges = [[0] * maxn for _ in range(maxn)]

# P1129 [ZJOI2007]矩阵游戏
def p1129(n, edges):
    def dfs(u):
        for v in range(n):
            if edges[u][v] and not vis[v]:
                vis[v] = 1
                if cy[v] == -1 or dfs(cy[v]):
                    cx[u], cy[v] = v, u
                    return 1
        return 0
    res = 0
    for u in range(n):
        if cx[u] == -1:
            for w in range(n): vis[w] = 0
            res += dfs(u)
    return res == n


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        for i in range(N):
            cx[i] = cy[i] = -1
            for j in range(N):
                edges[i][j] = 0
        s = 0
        for i in range(N):
            ln = sys.stdin.readline().strip()
            for j, x in enumerate(list(map(int, ln.split(' ')))):
                if x == 1:
                    s += 1
                    edges[i][j] = 1
        print(ans[s >= N and p1129(N, edges)])