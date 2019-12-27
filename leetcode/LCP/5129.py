# -*- coding: utf-8 -*-
# ======================================
# @File    : 5129.py
# @Time    : 2019/12/14 23:14
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5129. 下降路径最小和  II](https://leetcode-cn.com/problems/minimum-falling-path-sum-ii/)
    """
    @timeit
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        if n <= 1: return 0
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = arr[0][j]
        for i in range(1, n):
            mi1, mi2 = sorted([[dp[i-1][j], j] for j in range(n)])[:2]
            for j in range(n):
                if j != mi1[1]:
                    dp[i][j] = arr[i][j] + mi1[0]
                else:
                    dp[i][j] = arr[i][j] + mi2[0]
        return min([dp[-1][i] for i in range(n)])


if __name__ == '__main__':
    a = Solution()
    a.minFallingPathSum([[1,2,3],
                         [4,5,6],
                         [7,8,9]])