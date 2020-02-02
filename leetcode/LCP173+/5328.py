# -*- coding: utf-8 -*-
# ======================================
# @File    : 5328.py
# @Time    : 2020/2/2 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ctr = []
        n, m = len(mat), len(mat[0])
        for i in range(n):
            c = m
            for j in range(m):
                if mat[i][j] == 0:
                    c = j
                    break
            ctr.append([c, i])
        ctr.sort()
        return [e[1] for e in ctr[:k]]


if __name__ == '__main__':
    a = Solution()
    a.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3)