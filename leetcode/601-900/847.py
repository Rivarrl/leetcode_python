# -*- coding: utf-8 -*-
# ======================================
# @File    : 847.py
# @Time    : 2020/6/30 11:22 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [847. 访问所有节点的最短路径](https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes/)
    """
    @timeit
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        from collections import deque, defaultdict
        n = len(graph)
        stk = deque()
        dist = defaultdict(lambda: n*n)
        for i in range(n):
            stk.append((i, 1 << i))
            dist[i, 1 << i] = 0
        while stk:
            u, rec = stk.popleft()
            s = dist[u, rec]
            if rec + 1 == 1 << n:
                return s
            for v in graph[u]:
                if s + 1 < dist[v, rec | (1 << v)]:
                    dist[v, rec | (1 << v)] = s + 1
                    stk.append((v, rec | (1 << v)))
        return -1

if __name__ == '__main__':
    a = Solution()
    a.shortestPathLength([[1,2,3],[0],[0],[0]])
    a.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]])
    a.shortestPathLength([[1],[0,2,4],[1,3],[2],[1,5],[4]])