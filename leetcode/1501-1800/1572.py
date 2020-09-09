# -*- coding: utf-8 -*-
# ======================================
# @File    : 1572.py
# @Time    : 2020/9/9 23:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1572. 矩阵对角线元素的和](https://leetcode-cn.com/problems/matrix-diagonal-sum/)
    """
    @timeit
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i]
            if n-1-i == i: continue
            res += mat[i][n-1-i]
        return res

if __name__ == '__main__':
     a = Solution()
     a.diagonalSum(mat = [[1,2,3],
                        [4,5,6],
                        [7,8,9]])
     a.diagonalSum(mat = [[1,1,1,1],
                          [1,1,1,1],
                          [1,1,1,1],
                          [1,1,1,1]])