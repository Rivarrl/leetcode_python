# -*- coding: utf-8 -*-
# ======================================
# @File    : 1582.py
# @Time    : 2020/9/14 20:42
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1582. 二进制矩阵中的特殊位置](https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix/)
    """
    @timeit
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(x, y):
            for i in range(n):
                if i == x: continue
                if mat[i][y] == 1: return False
            for j in range(m):
                if j == y: continue
                if mat[x][j] == 1: return False
            return True
        n, m = len(mat), len(mat[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and check(i, j):
                    res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.numSpecial(mat = [[1,0,0],[0,0,1],[1,0,0]])
    a.numSpecial(mat = [[1,0,0],[0,1,0],[0,0,1]])
    a.numSpecial(mat = [[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]])
    a.numSpecial(mat = [[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]])