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


    @timeit
    def minFlips2(self, mat: List[List[int]]) -> int:
        # 看行/列，选一个短的，这里最大只有3，行列无所谓。把第一行的所有状态穷举出来，用位压缩。
        n, m = len(mat), len(mat[0])
        dxy = (0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)
        res = inv = n * m + 1
        for state in range(1 << n):
            step = 0
            tmp = [[0] * m for _ in range(n)]
            for j in range(m):
                if (state >> j) & 1:
                    step += 1
                    for dx, dy in dxy:
                        x, y = dx, j + dy
                        if 0 <= x < n and 0 <= y < m:
                            tmp[x][y] ^= 1
            for i in range(1, n):
                for j in range(m):
                    # 需要翻
                    if tmp[i-1][j] ^ mat[i-1][j]:
                        step += 1
                        for dx, dy in dxy:
                            x, y = i + dx, j + dy
                            if 0 <= x < n and 0 <= y < m:
                                tmp[x][y] ^= 1
            for j in range(m):
                if tmp[n-1][j] ^ mat[n-1][j]:
                    break
            else:
                res = min(res, step)
        return res == inv and -1 or res


if __name__ == '__main__':
    a = Solution()
    a.minFlips2([[0,0],[0,1]])
    a.minFlips2([[0]])
    a.minFlips2([[1,1,1],[1,0,1],[0,0,0]])
    a.minFlips2([[1,0,0],[1,0,0]])
