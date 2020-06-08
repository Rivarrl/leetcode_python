# -*- coding: utf-8 -*-
# ======================================
# @File    : 5431.py
# @Time    : 2020/6/7 11:27
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5431. 给房子涂色 III](https://leetcode-cn.com/problems/paint-house-iii/)
    """
    @timeit
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # 涂到第i个时造成了j个街区前一个涂的是k
        from functools import lru_cache
        inf = 0x3f3f3f3f
        @lru_cache(None)
        def f(i, j, k):
            if j > target: return inf
            if i == m:
                if j == target: return 0
                return inf
            if houses[i] > 0:
                if houses[i] != k:
                    return f(i+1, j+1, houses[i])
                else:
                    return f(i+1, j, k)
            else:
                res = inf
                for x in range(1, n+1):
                    if x == k:
                        res = min(res, f(i+1, j, k) + cost[i][k-1])
                    else:
                        res = min(res, f(i+1, j+1, x) + cost[i][x-1])
                return res
        res = f(0, 0, 0)
        return -1 if res == inf else res

    @timeit
    def minCost2(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp[i][j][k]表示涂到第i个房子刷出j个街区，并且前一个上色为k
        # houses[i]>0，当k==houses[i]时，dp[i][j][k]可更新dp[i+1][j][k]
        # 当k!=houses[i]时，dp[i][j][k]可更新dp[i+1][j+1][houses[i]]
        # houses[i]==0，dp[i][j][k]可更新dp[i+1][j][k]和dp[i+1][j+1][x!=k]
        inf = 0x3f3f3f3f
        dp = [[[inf] * (n+1) for _ in range(m+1)] for _ in range(m+1)]
        dp[0][0][0] = 0
        for i in range(m):
            for j in range(i+1):
                for k in range(n+1):
                    if houses[i]:
                        dp[i+1][j+(houses[i]!=k)][houses[i]] = min(dp[i+1][j+(houses[i]!=k)][houses[i]], dp[i][j][k])
                    else:
                        for x in range(1, n+1):
                            dp[i+1][j+(x!=k)][x] = min(dp[i+1][j+(x!=k)][x], dp[i][j][k] + cost[i][x-1])
        res = min(dp[m][target])
        return -1 if res == inf else res

if __name__ == '__main__':
    a = Solution()
    a.minCost2(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3)
    a.minCost2(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3)
    a.minCost2(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5)
    a.minCost2(houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3)
    a.minCost2([0,0,0,1], [[1,5],[4,1],[1,3],[4,4]], 4, 2, 4)