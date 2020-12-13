# -*- coding: utf-8 -*-
# ======================================
# @File    : 01-08.py
# @Time    : 2020/12/11 23:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 01.08. 零矩阵](https://leetcode-cn.com/problems/zero-matrix-lcci/)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        r, c = [1] * n, [1] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    r[i] = c[j] = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] *= r[i] * c[j]

if __name__ == '__main__':
    a = Solution()
    a.setZeroes([[1,1,1],
                  [1,0,1],
                  [1,1,1]])
    a.setZeroes([[0,1,2,0],
                  [3,4,5,2],
                  [1,3,1,5]])