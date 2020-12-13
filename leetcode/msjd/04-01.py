# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-01.py
# @Time    : 2020/12/13 0:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 04.01. 节点间通路](https://leetcode-cn.com/problems/route-between-nodes-lcci/)
    """
    @timeit
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        from collections import deque
        g = [set() for _ in range(n)]
        for u, v in graph:
            if u == v: continue
            g[u].add(v)
        stk = deque([start])
        seen = {start}
        while stk:
            u = stk.pop()
            if u == target: return True
            for v in g[u]:
                if v not in seen:
                    seen.add(v)
                    stk.appendleft(v)
        return False


if __name__ == '__main__':
    a = Solution()
    a.findWhetherExistsPath(n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2)
    a.findWhetherExistsPath(n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4)
    a.findWhetherExistsPath(12, [[0, 1], [1, 2], [1, 3], [1, 10], [1, 11], [1, 4], [2, 4], [2, 6], [2, 9], [2, 10], [2, 4], [2, 5], [2, 10], [3, 7], [3, 7], [4, 5], [4, 11], [4, 11], [4, 10], [5, 7], [5, 10], [6, 8], [7, 11], [8, 10]], 2, 3)