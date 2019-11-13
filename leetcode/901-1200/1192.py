# -*- coding: utf-8 -*-
# ======================================
# @File    : 1192.py
# @Time    : 2019/11/11 23:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1192. 查找集群内的「关键连接」](https://leetcode-cn.com/problems/critical-connections-in-a-network)
    """
    @timeit
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        思路：tarjan找桥
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        dfn, low = [-1] * n, [-1] * n
        res = []
        timestamp = 0
        def tarjan(u, parent):
            nonlocal timestamp
            timestamp += 1
            dfn[u] = low[u] = timestamp
            for v in graph[u]:
                if dfn[v] < 0:
                    tarjan(v, u)
                    low[u] = min(low[u], low[v])
                elif v != parent:
                    low[u] = min(low[u], dfn[v])
        tarjan(0, 0)
        print(dfn)
        print(low)
        vis = [0] * n
        def dfs(u):
            if vis[u]: return
            vis[u] = 1
            for v in graph[u]:
                if dfn[u] < low[v]: res.append([u, v])
                dfs(v)
        dfs(0)
        return res



if __name__ == '__main__':
    a = Solution()
    a.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
    a.criticalConnections(5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]])

