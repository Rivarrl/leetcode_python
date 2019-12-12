# -*- coding: utf-8 -*-
# ======================================
# @File    : 310.py
# @Time    : 2019/12/12 9:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [310. 最小高度树](https://leetcode-cn.com/problems/minimum-height-trees/)
    """
    @timeit
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        思路: 找出所有边缘点, 无向图的边缘点的边数为1, 向中心访问, 找到最深的一批点即为答案
        """
        graph = [list() for _ in range(n)]
        degree = [0] * n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            graph[u].append(v)
            graph[v].append(u)
        stk = [(u, 1) for u in range(n) if degree[u] == 1]
        vis = [0] * n
        step = 0
        while stk:
            u, step = stk.pop()
            vis[u] = step
            for v in graph[u]:
                degree[v] -= 1
                if degree[v] == 1:
                    stk.insert(0, (v, step+1))
        return [u for u in range(n) if vis[u] == step]

if __name__ == '__main__':
    a = Solution()
    a.findMinHeightTrees(1, [])
    a.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])
    a.findMinHeightTrees(2, [[0, 1]])
    a.findMinHeightTrees(3, [[0,1],[0,2]])
    a.findMinHeightTrees(n = 4, edges = [[1, 0], [1, 2], [1, 3]])
    a.findMinHeightTrees(n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
