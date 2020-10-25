# -*- coding: utf-8 -*-
# ======================================
# @File    : 5156.py
# @Time    : 2020/10/25 11:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        n, m = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]
        d = defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[matrix[i][j]].append([i, j])
        arr = sorted(d.keys())
        x_max, y_max = [0] * n, [0] * m
        for k in arr:
            bf = True
            rx, ry = set(), set()
            while bf:
                bf = False
                for i, j in d[k]:
                    res[i][j] = max(x_max[i], y_max[j]) + 1
                    if x_max[i] < res[i][j] - 1:
                        x_max[i] = res[i][j] - 1
                        bf = True
                    if y_max[j] < res[i][j] - 1:
                        y_max[j] = res[i][j] - 1
                        bf = True
                    rx.add(i)
                    ry.add(j)
            for i in rx:
                x_max[i] += 1
            for j in ry:
                y_max[j] += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.matrixRankTransform(matrix = [[1,2],[3,4]])
    a.matrixRankTransform(matrix = [[7,7],[7,7]])
    a.matrixRankTransform(matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]])
    a.matrixRankTransform(matrix = [[7,3,6],[1,4,5],[9,8,2]])
    a.matrixRankTransform([[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]])
    a.matrixRankTransform([[-37,-26,-47,-40,-13],[22,-11,-44,47,-6],[-35,8,-45,34,-31],[-16,23,-6,-43,-20],[47,38,-27,-8,43]])