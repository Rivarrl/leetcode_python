# -*- coding: utf-8 -*-
# ======================================
# @File    : 5356.py
# @Time    : 2020/3/15 10:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        col, row = [], []
        for i in range(n):
            col += [min(matrix[i])]
        for j in range(m):
            m = 0
            for i in range(n):
                m = max(m, matrix[i][j])
            row += [m]
        res = list(set(col).intersection(set(row)))
        return res

if __name__ == '__main__':
    a = Solution()
    a.luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]])
    a.luckyNumbers(matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]])
    a.luckyNumbers(matrix = [[7,8],[1,2]])