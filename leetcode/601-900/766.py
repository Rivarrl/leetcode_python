# -*- coding: utf-8 -*-
# ======================================
# @File    : 766
# @Time    : 2021/2/22 14:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [766. 托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix/)
    """
    @timeit
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m-1
        while i < n:
            k = matrix[i][j]
            x, y = i + 1, j + 1
            while x < n and y < m:
                if matrix[x][y] != k:
                    return False
                x += 1
                y += 1
            if j > 0:
                j -= 1
            else:
                i += 1
        return True

if __name__ == '__main__':
    a = Solution()
    a.isToeplitzMatrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]])
    a.isToeplitzMatrix(matrix = [[1,2],[2,2]])