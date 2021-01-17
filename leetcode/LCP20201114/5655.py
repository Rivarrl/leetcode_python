# -*- coding: utf-8 -*-
# ======================================
# @File    : 5655.py
# @Time    : 2021/1/17 10:48
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5655. 重新排列后的最大子矩阵](https://leetcode-cn.com/problems/largest-submatrix-with-rearrangements/)
    """
    @timeit
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
        res = 0
        for i in range(n):
            tmp = sorted(matrix[i], reverse=True)
            for j in range(m):
                res = max(res, tmp[j] * (j+1))
        return res



if __name__ == '__main__':
    a = Solution()
    a.largestSubmatrix(matrix = [[0,0,1],[1,1,1],[1,0,1]])
    a.largestSubmatrix(matrix = [[1,0,1,0,1]])
    a.largestSubmatrix(matrix = [[1,1,0],[1,0,1]])
    a.largestSubmatrix(matrix = [[0,0],[0,0]])