# -*- coding: utf-8 -*-
# ======================================
# @File    : 29.py
# @Time    : 2020/5/7 15:13
# @Author  : Rivarrl
# ======================================
# [面试题29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0: return []
        m = len(matrix[0])
        dxy = ((0,1), (1,0), (0,-1), (-1,0))
        l, r, u, d = 0, m-1, 0, n-1
        i = j = k = p = 0
        a = n * m
        res = []
        while p < a:
            dx, dy = dxy[k]
            x, y = i + dx, j + dy
            res.append(matrix[i][j])
            if u <= x <= d and l <= y <= r:
                i, j = x, y
            else:
                k = (k + 1) % 4
                if k == 1: u += 1
                elif k == 2: r -= 1
                elif k == 3: d -= 1
                else: l += 1
                dx, dy = dxy[k]
                i, j = i + dx, j + dy
            p += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    a.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])