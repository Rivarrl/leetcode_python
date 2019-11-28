# -*- coding: utf-8 -*-
# ======================================
# @File    : hungarian.py
# @Time    : 2019/11/28 15:43
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from graph.graph_utils import *

# 匈牙利算法
# 求二分图的最大匹配
# 利用增广路径的方法
# 有两个节点集合x和y，他们之间有些连接
# 定义一条连接两侧的节点与其他连接的两侧节点不重复，这样的连接叫做匹配，找出最多的满足该条件的连接（即最大匹配）

def hungarian(nx, ny, edges):
    def dfs(u):
        for v in range(ny):
            if edges[u][v] and not vis[v]:
                vis[v] = 1
                # v还没有被连接或是与v连接的w可以找到新的连接
                if cy[v] == -1 or dfs(cy[v]):
                    cx[u] = v
                    cy[v] = u
                    return 1
        return 0
    n = nx + ny
    cx, cy, vis = [-1] * nx, [-1] * ny, [0] * n
    res = 0
    for u in range(nx):
        if cx[u] == -1:
            for i in range(n): vis[i] = 0
            res += dfs(u)
    return res

if __name__ == '__main__':
    connections = [[0,0],[0,2],[1,1],[2,2],[2,3],[3,0]]
    n = 4
    edges = [[0] * n for _ in range(n)]
    for x, y in connections:
        edges[x][y] = 1
    res = hungarian(4, 4, edges)
    print(res)