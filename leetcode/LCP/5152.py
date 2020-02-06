# -*- coding: utf-8 -*-
# ======================================
# @File    : 5152.py
# @Time    : 1/25/20 10:48 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5152. 将矩阵按对角线排序](https://leetcode-cn.com/problems/sort-the-matrix-diagonally/)
    """
    @timeit
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        res = [[0]*m for _ in range(n)]
        for i in range(n):
            j, k = i, 0
            tmp = []
            while j < n and k < m:
                tmp.append(mat[j][k])
                j += 1
                k += 1
            tmp.sort()
            j, k = i, 0
            while j < n and k < m:
                res[j][k] = tmp[k]
                j += 1
                k += 1
        for j in range(1, m):
            i, k = j, 0
            tmp = []
            while k < n and i < m:
                tmp.append(mat[k][i])
                i += 1
                k += 1
            tmp.sort()
            i, k = j, 0
            while k < n and i < m:
                res[k][i] = tmp[k]
                i += 1
                k += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])