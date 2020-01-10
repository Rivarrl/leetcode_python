# -*- coding: utf-8 -*-
# ======================================
# @File    : 48
# @Time    : 2020/1/10 13:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [48. 旋转图像](https://leetcode-cn.com/problems/rotate-image/)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range(n//2 + (n & 1)):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]


if __name__ == '__main__':
    a = Solution()
    a.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])
    a.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])