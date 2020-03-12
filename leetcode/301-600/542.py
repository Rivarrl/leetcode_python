# -*- coding: utf-8 -*-
# ======================================
# @File    : 542.py
# @Time    : 2020/3/12 23:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [542. 01 矩阵](https://leetcode-cn.com/problems/01-matrix/)
    """
    @timeit
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import deque
        n, m = len(matrix), len(matrix[0])
        q = deque()
        res = [[-1]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    q.append((i, j, 0))
                    res[i][j] = 0
        dxy = ((0, 1), (-1, 0), (1, 0), (0, -1))
        while q:
            i, j, s = q.popleft()
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and res[x][y] == -1 and matrix[x][y] == 1:
                    res[x][y] = s + 1
                    q.append((x, y, s+1))
        return res


if __name__ == '__main__':
    a = Solution()
    a.updateMatrix([[0,0,0],
                    [0,1,0],
                    [0,0,0]])
    a.updateMatrix([[0,0,0],
                    [0,1,0],
                    [1,1,1]])