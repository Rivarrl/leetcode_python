# -*- coding: utf-8 -*-
# ======================================
# @File    : 1584.py
# @Time    : 2021/1/19 9:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1584. 连接所有点的最小费用](https://leetcode-cn.com/problems/min-cost-to-connect-all-points/)
    """
    @timeit
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        g = [[0] * n for _ in range(n)]
        dis = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        for i in range(n):
            for j in range(i+1, n):
                g[i][j] = g[j][i] = dis(points[i], points[j])
        inf = 0x3f3f3f3f
        vis = [False] * n
        d = [inf] * n
        d[0] = 0
        for i in range(1, n):
            d[i] = g[i][0]
        for i in range(1, n):
            x = 0
            for j in range(1, n):
                if not vis[j] and (x == 0 or d[j] < d[x]):
                    x = j
            vis[x] = True
            for y in range(n):
                if not vis[y]:
                    d[y] = min(d[y], g[x][y])
        res = 0
        for i in range(1, n):
            res += d[i]
        return res

if __name__ == '__main__':
    a = Solution()
    a.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]])
    a.minCostConnectPoints(points = [[3,12],[-2,5],[-4,1]])
    a.minCostConnectPoints(points = [[0,0],[1,1],[1,0],[-1,1]])
    a.minCostConnectPoints(points = [[-1000000,-1000000],[1000000,1000000]])
    a.minCostConnectPoints(points = [[0,0]])