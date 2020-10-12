# -*- coding: utf-8 -*-
# ======================================
# @File    : 1615.py
# @Time    : 2020/10/12 1:03 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1615. 最大网络秩](https://leetcode-cn.com/problems/maximal-network-rank/)
    """
    @timeit
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
        d = defaultdict(set)
        for u, v in roads:
            d[u].add(v)
            d[v].add(u)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res = max(len(d[i]) + len(d[j]) - int(j in d[i]), res)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]])
    a.maximalNetworkRank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])
    a.maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])