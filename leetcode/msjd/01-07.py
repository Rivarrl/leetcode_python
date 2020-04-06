# -*- coding: utf-8 -*-
# ======================================
# @File    : 01-07.py
# @Time    : 2020/4/7 0:18
# @Author  : Rivarrl
# ======================================
# [面试题 01.07. 旋转矩阵](https://leetcode-cn.com/problems/rotate-matrix-lcci/)
from algorithm_utils import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2+n%2):
            for j in range(n//2):
                i2, j2 = j, n - 1 - i
                i3, j3 = n - 1 - i, n - 1 - j
                i4, j4 = n - 1 - j, i
                matrix[i][j], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = matrix[i4][j4], matrix[i][j], matrix[i2][j2], matrix[i3][j3]

if __name__ == '__main__':
    a = Solution()
    a.rotate(matrix = [[1,2,3],
                      [4,5,6],
                      [7,8,9]])
    a.rotate(matrix = [[ 5, 1, 9,11],
                      [ 2, 4, 8,10],
                      [13, 3, 6, 7],
                      [15,14,12,16]])