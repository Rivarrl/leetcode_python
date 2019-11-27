# -*- coding: utf-8 -*-
# ======================================
# @File    : 1162.py
# @Time    : 2019/11/27 14:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1162. 地图分析](https://leetcode-cn.com/problems/as-far-from-land-as-possible/)
    """
    @timeit
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        思路：暴力求解，记录每个点向右向下最长的边
        """
        n, m = len(grid), len(grid[0])
        dp = [[None] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dp[i][j] = (0, 0)
                    continue
                k = i + 1
                while k < n:
                    if grid[k][j] == 0: break
                    k += 1
                ki = k - i
                k = j + 1
                while k < m:
                    if grid[i][k] == 0: break
                    k += 1
                kj = k - j
                dp[i][j] = (ki, kj)
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: continue
                x = min(dp[i][j][0], dp[i][j][1])
                while x > 0:
                    if dp[i+x-1][j][1] >= x and dp[i][j+x-1][0] >= x:
                        break
                    x -= 1
                res = max(res, x)
        return res ** 2


if __name__ == '__main__':
    a = Solution()
    # a.maxDistance([[1,1,1],[1,0,1],[1,1,1]])
    # a.maxDistance([[1,1,0,0]])
    # a.maxDistance([[0]])
    # a.maxDistance([[1,1,0],[1,1,1],[1,1,1],[1,1,1]])
    # a.maxDistance([[0,0],[1,1]])
    a.maxDistance([[1,1,0,1,1,1,1,0],
                   [0,1,1,0,0,0,1,1],
                   [1,0,1,1,1,1,1,1],
                   [1,1,1,0,0,1,1,1],
                   [1,0,1,0,1,1,1,0],
                   [1,1,1,1,1,1,1,1],
                   [0,1,1,1,0,1,1,1],
                   [0,1,1,0,1,1,0,1]])