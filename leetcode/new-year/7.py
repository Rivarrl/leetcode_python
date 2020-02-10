# -*- coding: utf-8 -*-
# ======================================
# @File    : 7.py
# @Time    : 1/18/20 1:27 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

import heapq

class Node:
    def __init__(self, u, v, w = 1, nxt = None):
        self.u = u
        self.v = v
        self.w = w
        self.next = nxt

    def __lt__(self, other):
        return self.w < other.w

inf = 0x3f3f3f3f

class Solution:
    """
    [100272. 🐭年快乐](https://leetcode-cn.com/contest/sf-2020/problems/happy-new-year-lol/)
    """
    @timeit
    def happy(self, n: int, roads: List[List[int]], codes: List[str]) -> str:
        graph = self._linked_list(n, roads)
        self.codes = codes
        return self.dijkstra(n, graph, 11)

    def _linked_list(self, n, connections):
        # direction 有向无向 0 无向，1 有向
        # weights 点权 None 无权，list(int) 带权
        def build_connections(a, b, c):
            node = Node(a, b)
            node.w = c
            if not arr[a]:
                arr[a] = node
            else:
                p = arr[a]
                while p.next:
                    p = p.next
                p.next = node

        arr = [None] * n
        for i in range(len(connections)):
            a, b = connections[i][0], connections[i][1]
            c = connections[i][2]
            build_connections(a, b, c)
            build_connections(b, a, c)
        return arr

    def dijkstra(self, n, graph, s):
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
        dist_to = [inf] * n
        dist_to[s] = 0
        pq = []
        heapq.heappush(pq, (0.0, s))
        while pq:
            w, u = heapq.heappop(pq)
            relax(u)
        return self.display(n, s, dist_to, edge_to)

    def display(self, n, s, dist_to, edge_to):
        paths = [list() for _ in range(n)]
        for v in range(n):
            if v != s and dist_to[v] != inf:
                e = edge_to[v]
                while e:
                    paths[v].append(e)
                    e = edge_to[e.u]
        res = ''
        for i, path in enumerate(paths):
            if not path: continue
            if path[0].v != 0: continue
            for j in range(len(path)-1, -1, -1):
                e = path[j]
                res += self.codes[e.u]
                if j == 0:
                    res += self.codes[e.v]
            break
        return res

if __name__ == '__main__':
    a = Solution()