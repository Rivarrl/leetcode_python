# -*- coding: utf-8 -*-
# ======================================
# @File    : 1478.py
# @Time    : 2020/7/24 1:56 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1478. 安排邮筒](https://leetcode-cn.com/problems/allocate-mailboxes/)
    """
    @timeit
    def minDistance(self, houses: List[int], m: int) -> int:
        # dp[i][j]表示前i+1个房子用j个邮筒的最优解
        # i～j用1个邮筒时，摆在中位数为最优解
        # dp[i][j] = min(dp[k-1][j-1] + f[k][i] for k := [j-1, i])
        houses.sort()
        n = len(houses)
        dp = [[0x3f3f3f3f] * (m+1) for _ in range(n)]
        f = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mi = i + j >> 1
                for k in range(i, j+1):
                    f[i][j] += abs(houses[k] - houses[mi])
        for i in range(n): dp[i][1] = f[0][i]
        for i in range(n):
            for j in range(2, min(m, i+1) + 1):
                for k in range(j-1, i+1):
                    dp[i][j] = min(dp[k-1][j-1] + f[k][i], dp[i][j])
        return dp[-1][-1] < 0x3f3f3f3f and dp[-1][-1] or 0

if __name__ == '__main__':
    a = Solution()
    a.minDistance(houses = [1,4,8,10,20], m = 3)
    a.minDistance(houses = [2,3,5,12,18], m = 2)
    a.minDistance(houses = [7,4,6,1], m = 1)
    a.minDistance(houses = [3,6,14,10], m = 4)
    a.minDistance([5,18,25,27,28,13,9,12,22], 7)