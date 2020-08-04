# -*- coding: utf-8 -*-
# ======================================
# @File    : 1466.py
# @Time    : 2020/6/1 18:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1466. 重新规划路线](https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)
    """
    @timeit
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        g = defaultdict(list)
        vg = defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
            vg[u].append(v)
        stk = [0]
        vis = [False] * n
        vis[0] = True
        res = 0
        while stk:
            u = stk.pop()
            for v in g[u]:
                if not vis[v]:
                    vis[v] = True
                    stk.append(v)
                    if v in vg[u]:
                        res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]])
    a.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]])
    a.minReorder(n = 3, connections = [[1,0],[2,0]])