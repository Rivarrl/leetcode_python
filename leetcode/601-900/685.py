# -*- coding: utf-8 -*-
# ======================================
# @File    : 685.py
# @Time    : 2020/9/17 12:55 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class UnionFind:
    """
    并查集
    """
    def __init__(self, n):
        self.arr = list(range(n))

    def union(self, i: int, j: int):
        self.arr[self.find(i)] = self.find(j)

    def find(self, i: int) -> int:
        if self.arr[i] != i:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]

class Solution:
    """
    [685. 冗余连接 II](https://leetcode-cn.com/problems/redundant-connection-ii/)
    """
    @timeit
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)
        degree_in = defaultdict(int)
        N = st = dl = 0
        for u, v in edges:
            graph[u].append(v)
            degree_in[v] += 1
            N = max(N, u, v)
        for i in range(1, N+1):
            if degree_in[i] == 0:
                st = i
            elif degree_in[i] == 2:
                dl = i
        def ok(u):
            for v in graph[u]:
                if seen[v] == 0:
                    seen[v] = 1
                    ok(v)
            return all(e == 1 for e in seen[1:])
        if st > 0:
            for u, v in edges[::-1]:
                if v != dl: continue
                graph[u].remove(v)
                seen = [0] * (N+1)
                seen[st] = 1
                if ok(st): return [u, v]
                graph[u].append(v)
        else:
            for u, v in edges[::-1]:
                graph[u].remove(v)
                seen = [0] * (N+1)
                seen[v] = 1
                if ok(v): return [u, v]
                graph[u].append(v)
        return [-1, -1]

    @timeit
    def findRedundantDirectedConnection2(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1)
        parent = list(range(n + 1))
        conflict = -1
        cycle = -1
        # u->v
        for i, (u, v) in enumerate(edges):
            if parent[v] != v:
                conflict = i
            else:
                parent[v] = u
                if uf.find(u) == uf.find(v):
                    cycle = i
                else:
                    uf.union(u, v)

        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflict_edge = edges[conflict]
            if cycle >= 0:
                return [parent[conflict_edge[1]], conflict_edge[1]]
            else:
                return [conflict_edge[0], conflict_edge[1]]


if __name__ == '__main__':
    a = Solution()
    a.findRedundantDirectedConnection([[1,2], [1,3], [2,3]])
    a.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]])
    a.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]])