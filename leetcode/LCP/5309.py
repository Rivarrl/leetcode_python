# -*- coding: utf-8 -*-
# ======================================
# @File    : 5309
# @Time    : 2020/1/12 14:07
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5309. 连通网络的操作次数]()
    """
    @timeit
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        nc = len(connections)
        if n - 1 > nc: return -1
        idx = [i for i in range(n)]
        def find(p):
            if idx[p] != p:
                idx[p] = find(idx[p])
            return idx[p]
        def union(p, q):
            x, y = find(p), find(q)
            if x == y: return 1
            idx[y] = x
            return 0
        for p, q in connections:
            union(p, q)
        d = set()
        for p in range(n):
            x = find(p)
            if x not in d:
                d.add(x)
        return len(d) - 1


if __name__ == '__main__':
    a = Solution()
    # a.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]])
    # a.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]])
    # a.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]])
    # a.makeConnected(n = 5, connections = [[0,1],[0,2],[3,4],[2,3]])
    a.makeConnected(11, [[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]])