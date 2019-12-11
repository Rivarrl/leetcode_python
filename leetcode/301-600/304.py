# -*- coding: utf-8 -*-
# ======================================
# @File    : 304.py
# @Time    : 2019/12/11 11:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class NumMatrix:
    """
    [304. 二维区域和检索 - 矩阵不可变](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/)
    思路: 二维数组的前缀和
    """
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        self.N = n
        if n > 0:
            m = len(matrix[0])
            self.M = m
            if m > 0:
                self.pre = [[0] * (m+1) for _ in range(n+1)]
                for i in range(n):
                    for j in range(m):
                        self.pre[i+1][j+1] += self.pre[i+1][j] + self.pre[i][j+1] - self.pre[i][j] + matrix[i][j]

    @timeit
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 < 0 or row2 < row1 or row2 >= self.N or col1 < 0 or col2 < col1 or col2 > self.M: return 0
        return self.pre[row2+1][col2+1] - self.pre[row1][col2+1] - self.pre[row2+1][col1] + self.pre[row1][col1]


if __name__ == '__main__':
    # Your NumMatrix object will be instantiated and called as such:
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    matrix_pretty_print(matrix)
    matrix_pretty_print(obj.pre)
    obj.sumRegion(2, 1, 4, 3)
    obj.sumRegion(1, 1, 2, 2)
    obj.sumRegion(1, 2, 2, 4)
