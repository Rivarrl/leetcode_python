# -*- coding: utf-8 -*-
# ======================================
# @File    : 797.py
# @Time    : 2019/11/21 0:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [797. 所有可能的路径](https://leetcode-cn.com/problems/all-paths-from-source-to-target/)
    """
    @timeit
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        思路：有向无环图的路径，dfs即可
        """
        def dfs(u):
            if degree_out[u] == 0:
                return [[u]]
            res = []
            for v in graph[u]:
                for x in dfs(v):
                    res += [[u] + x]
            return res

        n = len(graph)
        degree_in = [0] * n
        degree_out = [0] * n
        for u in range(n):
            degree_out[u] = len(graph[u])
            for v in graph[u]:
                degree_in[v] += 1
        res = []
        for u in range(n):
            if degree_in[u] == 0:
                res += dfs(u)
        return res


if __name__ == '__main__':
    a = Solution()
    a.allPathsSourceTarget([[1,2], [3], [3], []])