# -*- coding: utf-8 -*-
# ======================================
# @File    : 54.py
# @Time    : 2020/5/7 15:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [54. 螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix/)
    """
    @timeit
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0: return []
        m = len(matrix[0])
        inf = 1 << 32
        i, j, dx, dy = 0, 0, 0, 1
        res = []
        ok = lambda x, y: 0 <= x < n and 0 <= y < m
        for _ in range(n * m):
            res.append(matrix[i][j])
            matrix[i][j] = inf
            if not ok(i+dx, j+dy) or matrix[i+dx][j+dy] == inf:
                dx, dy = dy, -dx
            i, j = i+dx, j+dy
        return res


if __name__ == '__main__':
    a = Solution()
    a.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    a.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])