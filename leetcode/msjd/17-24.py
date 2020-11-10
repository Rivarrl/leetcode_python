# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-24.py
# @Time    : 2020/10/25 10:17
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.24. 最大子矩阵](https://leetcode-cn.com/problems/max-submatrix-lcci/)
    """
    @timeit
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        res = [0] * 4
        m = matrix[0][0]
        n, m = len(matrix), len(matrix[0])
        for r1 in range(n):
            dp = [0] * m
            for r2 in range(r1, n):
                dp[]


if __name__ == '__main__':
    a = Solution()
    a.getMaxMatrix([[-1, 0], [0, -1]])
    a.getMaxMatrix([[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]])