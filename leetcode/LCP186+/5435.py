# -*- coding: utf-8 -*-
# ======================================
# @File    : 5435.py
# @Time    : 2020/6/27 22:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        from collections import defaultdict
        if k == 1: return n
        g = defaultdict(list)
        d = {}
        for u, v in dependencies:
            g[u].append(v)
            d[u] = d.get(u, 0)
            d[v] = d.get(v, 0) + 1
        stk = [(e, 0) for e in d if d[e] == 0]
        res = 0
        c = last = 0
        vis = [0] * (n + 1)
        fill = 0
        while stk:
            u, step = stk.pop(0)
            vis[u] = 1
            if step > last:
                res += (c > 0)
                fill += (k - c)
                c = 0
                last = step
            c += 1
            if c == k:
                res += 1
                c = 0
            for v in g[u]:
                if d[v] > 0:
                    d[v] -= 1
                    if d[v] == 0:
                        stk.append((v, step + 1))
        if c > 0:
            res += 1
            fill += (k - c)
        rr = sum(1 for x in vis[1:] if x == 0)
        rr = max(0, rr - fill)
        print(fill)
        res += (rr // k + rr % k)
        return res

if __name__ == '__main__':
    a = Solution()
    # a.minNumberOfSemesters(n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2)
    # a.minNumberOfSemesters(n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2)
    # a.minNumberOfSemesters(n = 11, dependencies = [], k = 2)
    # a.minNumberOfSemesters(n = 5, dependencies = [[3,1]], k = 4)
    # a.minNumberOfSemesters(n = 4, dependencies = [[2,1], [2,4]], k=2)
    # a.minNumberOfSemesters(n = 4, dependencies = [[1,2], [4,2]], k=1)
    a.minNumberOfSemesters(n = 8, dependencies = [[1,6],[2,7],[8,7],[2,5],[3,4]], k = 3)