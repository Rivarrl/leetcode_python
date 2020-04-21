# -*- coding: utf-8 -*-
# ======================================
# @File    : 661.py
# @Time    : 2020/4/21 19:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        n, m = len(M), len(M[0])
        res = [[0] * m for _ in range(n)]
        def avg(i, j):
            r = c = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m:
                        r += M[x][y]
                        c += 1
            return r // c

        for i in range(n):
            for j in range(m):
                res[i][j] = avg(i, j)
        return res

if __name__ == '__main__':
    a = Solution()
    a.imageSmoother([[1,1,1],
                     [1,0,1],
                     [1,1,1]])