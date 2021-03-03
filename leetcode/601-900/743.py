# -*- coding: utf-8 -*-
# ======================================
# @File    : 743.py
# @Time    : 2021/3/2 22:23
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [743. 网络延迟时间](https://leetcode-cn.com/problems/network-delay-time/)
    """
    @timeit
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        g = [[101] * (n+1) for _ in range(n+1)]
        for u, v, w in times:
            g[u][v] = w
        res = [101] * (n+1)
        stk = [[0, k]]
        while stk:
            t, u = heapq.heappop(stk)
            if res[u] < 101: continue
            res[u] = t
            for v, w in enumerate(g[u]):
                if res[v] == 101 and w < 101:
                    heapq.heappush(stk, [t+w, v])
        ret = max(res[1:])
        return ret if ret < 101 else -1


if __name__ == '__main__':
    a = Solution()
    a.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
    a.networkDelayTime(times = [[1,2,1]], n = 2, k = 1)
    a.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)
    a.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1)