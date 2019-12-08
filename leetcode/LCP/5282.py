# -*- coding: utf-8 -*-
# ======================================
# @File    : 5282.py
# @Time    : 2019/12/8 11:10
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5282. 转化为全零矩阵的最少反转次数
    """
    @timeit
    def minFlips(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        def to_tuple(arr):
            tp = tuple()
            for i in range(n):
                st = tuple(arr[i])
                tp += (st, )
            return tp
        dxy = (0, 1), (0, -1), (1, 0), (-1, 0)
        def change(arr, i, j):
            nst = [[arr[i][j] for j in range(m)] for i in range(n)]
            nst[i][j] ^= 1
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    nst[x][y] ^= 1
            return nst
        stk = [(mat, 0)]
        vis = {to_tuple(mat)}
        while stk:
            state, step = stk.pop()
            if sum((sum(e) for e in state)) == 0: return step
            for i in range(n):
                for j in range(m):
                    nst = change(state, i, j)
                    tpnst = to_tuple(nst)
                    if not tpnst in vis:
                        vis.add(tpnst)
                        stk.insert(0, (nst, step+1))
        return -1

if __name__ == '__main__':
    a = Solution()
    a.minFlips([[0,0],[0,1]])
    a.minFlips([[0]])
    a.minFlips([[1,1,1],[1,0,1],[0,0,0]])
    a.minFlips([[1,0,0],[1,0,0]])
