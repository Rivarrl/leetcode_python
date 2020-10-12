# -*- coding: utf-8 -*-
# ======================================
# @File    : 1617.py
# @Time    : 2020/10/12 1:35 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [1617. 统计子树中城市之间最大距离](https://leetcode-cn.com/problems/count-subtrees-with-max-distance-between-cities/)
    """
    @timeit
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import deque
        g = {}
        for u, v in edges:
            g[u - 1] = g.get(u - 1, []) + [v - 1]
            g[v - 1] = g.get(v - 1, []) + [u - 1]
        def bfs(p, st):
            stk = deque([[p, 0]])
            seen = 0
            res, q = 0, p
            while stk:
                u, s = stk.popleft()
                if res < s:
                    res = s
                    q = u
                for v in g[u]:
                    if (1 << v) & st and seen & (1 << v) == 0:
                        seen |= (1 << v)
                        stk.append([v, s+1])
            return res, q, seen
        def start(s):
            if s == 0: return -1
            r = 0
            while s & 1 == 0:
                s >>= 1
            return r
        res = [0] * n
        for st in range(1, 1 << n):
            if st & (st - 1) == 0: continue
            p = start(st)
            r, q, seen = bfs(p, st)
            if seen != st: continue
            if q != p:
                r, _, _ = bfs(q, st)
            res[r] += 1
        return res[1:]

if __name__ == '__main__':
    a = Solution()
    a.countSubgraphsForEachDiameter(n=4, edges=[[1, 2], [2, 3], [2, 4]])
    # a.countSubgraphsForEachDiameter(n=2, edges=[[1, 2]])
    # a.countSubgraphsForEachDiameter(n=3, edges=[[1, 2], [2, 3]])
    # a.countSubgraphsForEachDiameter(4, [[1,3],[1,4],[2,3]])
