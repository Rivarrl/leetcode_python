# -*- coding: utf-8 -*-
# ======================================
# @File    : s2.py
# @Time    : 2020/4/18 15:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        from collections import defaultdict
        g = defaultdict(set)
        for x, y in relation:
            g[x].add(y)
        stk = [(0, 0)]
        res = 0
        while stk:
            i, s = stk.pop(0)
            if s == k and i == n - 1:
                res += 1
            elif s < k:
                for j in g[i]:
                    stk.append((j, s+1))
        return res

if __name__ == '__main__':
    a = Solution()
    a.numWays(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3)
    a.numWays(n = 3, relation = [[0,2],[2,1]], k = 2)