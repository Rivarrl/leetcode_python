# -*- coding: utf-8 -*-
# ======================================
# @File    : 10-09.py
# @Time    : 2020/11/25 0:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 10.09. 排序矩阵查找](https://leetcode-cn.com/problems/sorted-matrix-search-lcci/)
    """
    @timeit
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从左下角开始走，类似于二分查找
        n = len(matrix)
        if n == 0: return False
        m = len(matrix[0])
        i, j = n-1, 0
        while i >= 0 and j < m:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -=1
            else:
                return True
        return False


if __name__ == '__main__':
    a = Solution()
    x = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    a.searchMatrix(x, 5)
    a.searchMatrix(x, 20)