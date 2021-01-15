# -*- coding: utf-8 -*-
# ======================================
# @File    : 947.py
# @Time    : 2021/1/15 9:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [947. 移除最多的同行或同列石头](https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/)
    """
    @timeit
    def removeStones(self, stones: List[List[int]]) -> int:
        from collections import defaultdict, Counter
        ctx, cty = defaultdict(list), defaultdict(list)
        for u, (x, y) in enumerate(stones):
            ctx[x].append(u)
            cty[y].append(u)
        g = defaultdict(list)
        n = len(stones)
        for u, (x, y) in enumerate(stones):
            for v in ctx[x]:
                g[u].append(v)
            for v in cty[y]:
                g[u].append(v)
        dsu = [i for i in range(n)]
        def find(u):
            if dsu[u] != u:
                dsu[u] = find(dsu[u])
            return dsu[u]
        def union(u, v):
            x, y = find(u), find(v)
            if x != y:
                dsu[x] = y
        for u in range(n):
            for v in g[u]:
                union(u, v)
        for u in range(n): find(u)
        return n - len(Counter(dsu))

if __name__ == '__main__':
    a = Solution()
    a.removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
    a.removeStones(stones = [[0,0],[0,2],[1,1],[2,0],[2,2]])
    a.removeStones(stones = [[0,0]])
    a.removeStones([[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]])