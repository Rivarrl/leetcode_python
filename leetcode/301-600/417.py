# -*- coding: utf-8 -*-
# ======================================
# @File    : 417.py
# @Time    : 2020/7/28 3:39 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [417. 太平洋大西洋水流问题](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/)
    """
    @timeit
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # dfs 5%
        n = len(matrix)
        if n == 0: return []
        m = len(matrix[0])
        sea = [[0]*m for _ in range(n)]
        seen = [[0]*m for _ in range(n)]
        dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(i, j):
            if sea[i][j] < 3:
                if i == 0 or j == 0:
                    sea[i][j] |= 1
                if i == n-1 or j == m-1:
                    sea[i][j] |= 2
                for dx, dy in dxy:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and matrix[x][y] <= matrix[i][j] and seen[x][y] == 0:
                        seen[x][y] = 1
                        sea[i][j] |= dfs(x, y)
                        seen[x][y] = 0
                    if sea[i][j] == 3: break
            return sea[i][j]
        for i in range(n):
            for j in range(m):
                if sea[i][j] < 3:
                    dfs(i, j)
        return [[i, j] for i in range(n) for j in range(m) if sea[i][j] == 3]


    @timeit
    def pacificAtlantic2(self, matrix: List[List[int]]) -> List[List[int]]:
        # bfs 从边缘向中心更新
        from collections import deque
        n = len(matrix)
        if n == 0: return []
        m = len(matrix[0])
        sea = [[0]*m for _ in range(n)]
        queue = deque()
        for i in range(n):
            sea[i][0] |= 1
            sea[i][-1] |= 2
            queue.append((i, 0))
            queue.append((i, m-1))
        for j in range(m):
            sea[0][j] |= 1
            sea[-1][j] |= 2
            queue.append((0, j))
            queue.append((n-1, j))
        dxy = ((0, -1), (1, 0), (0, 1), (-1, 0))
        while queue:
            i, j = queue.popleft()
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and matrix[x][y] >= matrix[i][j] and sea[x][y] | sea[i][j] != sea[x][y]:
                    sea[x][y] |= sea[i][j]
                    queue.append((x, y))
        return [[i, j] for i in range(n) for j in range(m) if sea[i][j] == 3]


if __name__ == '__main__':
    a = Solution()
    a.pacificAtlantic([[1,2,2,3,5],
                       [3,2,3,4,4],
                       [2,4,5,3,1],
                       [6,7,1,4,5],
                       [5,1,1,2,4]])
    a.pacificAtlantic2([[1,2,2,3,5],
                       [3,2,3,4,4],
                       [2,4,5,3,1],
                       [6,7,1,4,5],
                       [5,1,1,2,4]])
    a.pacificAtlantic2([[1,1],[1,1],[1,1]])