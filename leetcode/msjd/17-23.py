# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-23.py
# @Time    : 2020/11/5 8:16 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.23. 最大黑方阵](https://leetcode-cn.com/problems/max-black-square-lcci/)
    """
    @timeit
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        from collections import defaultdict
        if not matrix:
            return []
        row = defaultdict(int)
        col = defaultdict(int)
        n = len(matrix)
        res = []
        for r in range(n-1, -1, -1):
            for c in range(n-1, -1, -1):
                if matrix[r][c] == 0:
                    row[r, c] = 1 + row[r, c + 1]
                    col[r, c] = 1 + col[r + 1, c]
        for r in range(n):
            for c in range(n):
                if matrix[r][c] == 0:
                    m = min(row[r, c], col[r, c])
                    i = 0 if not res else res[2]
                    for size in range(m, i, -1):
                        if col[r, c + size - 1] >= size and row[r + size - 1, c] >= size:
                            res = [r, c, size]
                            break
        return res

if __name__ == '__main__':
    a = Solution()
    a.findSquare([[1,0,1],
                  [0,0,1],
                  [0,0,1]])
    a.findSquare([[0,1,1],
                  [1,0,1],
                  [1,1,0]])
    a.findSquare([[1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
                  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                  [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                  [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                  [0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
                  [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 0, 1, 0, 0, 1, 1, 1]])
    a.findSquare([[1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
                  [0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
                  [0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
                  [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                  [1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
                  [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                  [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                  [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                  [1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]])