# -*- coding: utf-8 -*-
# ======================================
# @File    : 5347.py
# @Time    : 2020/3/1 13:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5347. 使网格图至少有一条有效路径的最小代价](https://leetcode-cn.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
    """
    @timeit
    def minCost(self, grid: List[List[int]]) -> int:
        # SPFA
        n, m = len(grid), len(grid[0])
        stk = [(0,0)]
        inf = 0x3f3f3f3f
        dp = [[inf] * m for _ in range(n)]
        vis = [[0] * m for _ in range(n)]
        dxy = [None, (0, 1), (0, -1), (1, 0), (-1, 0)]
        dp[0][0] = 0
        while stk:
            i, j = stk.pop()
            vis[i][j] = 0
            for k in range(1, 5):
                dx, dy = dxy[k]
                r, c = i + dx, j + dy
                p = [1, 0][grid[i][j] == k]
                if 0 <= r < n and 0 <= c < m:
                    if dp[r][c] > dp[i][j] + p:
                        dp[r][c] = dp[i][j] + p
                        if vis[r][c] == 0:
                            stk.insert(0, (r, c))
                            vis[r][c] = 1
        return dp[-1][-1] % inf


if __name__ == '__main__':
    a = Solution()
    a.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])
    a.minCost([[1,1,3],[3,2,2],[1,1,4]])
    a.minCost([[1,2],[4,3]])
    a.minCost([[2,2,2],[2,2,2]])
    a.minCost([[4]])
    a.minCost([[1,3,3,3],
               [2,2,1,2],
               [4,3,3,4],
               [3,2,2,3],
               [3,2,1,3],
               [4,1,4,3],
               [3,3,1,2]])