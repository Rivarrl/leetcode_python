# -*- coding: utf-8 -*-
# ======================================
# @File    : 867
# @Time    : 2021/2/25 13:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [867. 转置矩阵](https://leetcode-cn.com/problems/transpose-matrix/)
    """
    @timeit
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        if n == 0: return matrix
        m = len(matrix[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = matrix[j][i]
        return res

if __name__ == '__main__':
    a = Solution()
    a.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    a.transpose(matrix = [[1,2,3],[4,5,6]])