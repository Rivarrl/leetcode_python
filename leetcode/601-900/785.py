# -*- coding: utf-8 -*-
# ======================================
# @File    : 785.py
# @Time    : 2020/7/16 10:16 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [785. 判断二分图](https://leetcode-cn.com/problems/is-graph-bipartite/)
    """
    @timeit
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        valid = True
        def dfs(u, c):
            nonlocal valid
            color[u] = c
            nc = 0 if c == 1 else 1
            for v in graph[u]:
                if color[v] == -1:
                    dfs(v, nc)
                    if not valid:
                        return
                elif color[v] != nc:
                    valid = False
                    return
        for i in range(n):
            if color[i] == -1:
                dfs(i, 1)
                if not valid:
                    break
        return valid

if __name__ == '__main__':
    a = Solution()
    a.isBipartite([[1,3], [0,2], [1,3], [0,2]])
    a.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])