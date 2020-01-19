# -*- coding: utf-8 -*-
# ======================================
# @File    : 5144
# @Time    : 2020/1/11 22:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5144. 矩阵区域和]()
    """
    @timeit
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        pre = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] = pre[i][j+1] + pre[i+1][j] + mat[i][j] - pre[i][j]
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                li, ri = max(i-K, 0), min(i + K, n-1) + 1
                lj, rj = max(j-K, 0), min(j + K, m-1) + 1
                res[i][j] = pre[ri][rj] - pre[ri][lj] - pre[li][rj] + pre[li][lj]
        return res


if __name__ == '__main__':
    a = Solution()
    a.matrixBlockSum(mat = [[1,2,3],
                            [4,5,6],
                            [7,8,9]], K = 1)
    a.matrixBlockSum(mat = [[1,2,3],
                            [4,5,6],
                            [7,8,9]], K = 2)