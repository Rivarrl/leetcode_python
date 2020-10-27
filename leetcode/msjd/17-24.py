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
        n, m = len(matrix), len(matrix[0])
        pre = [[0] * (m+1) for _ in range(n+1)]
        res = [-1,-1,-1,-1]
        mx = -0x3f3f3f3f
        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] += pre[i+1][j] + matrix[i][j]
        for j in range(1, m+1):
            for i in range(1, n+1):
                pre[i][j] += pre[i-1][j]
        for xi in range(n):
            for xj in range(m):
                for yi in range(xi, n):
                    for yj in range(xj, m):
                        cur = pre[yi+1][yj+1] + pre[xi][xj] - pre[xi][yj+1] - pre[yi+1][xj]
                        if mx < cur:
                            mx = cur
                            res = [xi, xj, yi, yj]
        return res

if __name__ == '__main__':
    a = Solution()
    a.getMaxMatrix([[-1, 0], [0, -1]])
    a.getMaxMatrix([[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]])