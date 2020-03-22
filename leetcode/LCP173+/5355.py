# -*- coding: utf-8 -*-
# ======================================
# @File    : 5355.py
# @Time    : 2020/3/8 11:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1377. T 秒后青蛙的位置](https://leetcode-cn.com/problems/frog-position-after-t-seconds/)
    """
    @timeit
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        from collections import defaultdict
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        stk = [(1, 1, 0)]
        vis = set()
        vis.add(1)
        while stk:
            u, p, s = stk.pop(0)
            k = len([e for e in g[u] if not e in vis])
            if u == target:
                return 0 if s < t and k > 0 else p
            if s < t:
                for v in g[u]:
                    if not v in vis:
                        vis.add(v)
                        stk.append((v, p/k, s+1))
        return 0


if __name__ == '__main__':
    a = Solution()
    # a.frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4)
    # a.frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7)
    # a.frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6)
    # a.frogPosition(3,[[2,1],[3,2]],1,2)
    # a.frogPosition(8,[[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]],7,7)
    a.frogPosition(9,[[2,1],[3,1],[4,2],[5,3],[6,5],[7,4],[8,7],[9,7]],1,8)