# -*- coding: utf-8 -*-
# ======================================
# @File    : 240.py
# @Time    : 2019/11/9 21:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def searchMatrix(self, matrix:List[List[int]], target:int) -> bool:
        """
        [240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)
        思路：由左向右升序，由上向下升序，说明matrix[0][0]和matrix[-1][-1]就是答案的上下界，二分查找
        """
        n = len(matrix)
        if n == 0: return False
        m = len(matrix[0])
        i, j = n - 1, 0
        while i >= 0 and j < m:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False



if __name__ == '__main__':
    sol = Solution()
    matrix = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
             ]
    sol.searchMatrix(matrix, 5) # True
    sol.searchMatrix(matrix, 20) # False
