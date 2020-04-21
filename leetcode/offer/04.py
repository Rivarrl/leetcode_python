# -*- coding: utf-8 -*-
# ======================================
# @File    : 04.py
# @Time    : 2020/4/21 12:32
# @Author  : Rivarrl
# ======================================
# [面试题04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 从矩阵右上角开始，按二叉搜索树做
        n = len(matrix)
        if n == 0: return False
        m = len(matrix[0])
        if m == 0: return False
        x, y = 0, m-1
        while 0 <= x < n and 0 <= y < m:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x += 1
            else:
                y -= 1
        return False

if __name__ == '__main__':
    a = Solution()
    a.findNumberIn2DArray([[1,   4,  7, 11, 15],
                          [2,   5,  8, 12, 19],
                          [3,   6,  9, 16, 22],
                          [10, 13, 14, 17, 24],
                          [18, 21, 23, 26, 30]], 5)
    a.findNumberIn2DArray([[1,   4,  7, 11, 15],
                          [2,   5,  8, 12, 19],
                          [3,   6,  9, 16, 22],
                          [10, 13, 14, 17, 24],
                          [18, 21, 23, 26, 30]], 20)
    a.findNumberIn2DArray([[]],1)
