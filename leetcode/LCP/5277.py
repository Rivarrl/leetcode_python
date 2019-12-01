# -*- coding: utf-8 -*-
# ======================================
# @File    : 5277.py
# @Time    : 2019/12/1 10:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5277. 统计全为 1 的正方形子矩阵
    dp，计算以matrix[i][j]为右下角的正方形最大边长
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    最后对dp数组求和即可
    """
    @timeit
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
        return sum(sum(dp[i+1]) for i in range(n))

if __name__ == '__main__':
    a = Solution()
    a.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])
    a.countSquares([[1,0,1],[1,1,0],[1,1,0]])
