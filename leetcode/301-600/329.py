# -*- coding: utf-8 -*-
# ======================================
# @File    : 329.py
# @Time    : 2020/7/26 2:07
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [329. 矩阵中的最长递增路径](https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/)
    """
    @timeit
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        visited = [[0] * m for _ in range(n)]
        xy = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(i, j):
            if visited[i][j] > 0:
                return visited[i][j]
            cur = 0
            for x, y in xy:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    cur = max(cur, dfs(ni, nj))
            visited[i][j] = cur + 1
            return visited[i][j]

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        return ans



if __name__ == '__main__':
    a = Solution()
    a.longestIncreasingPath([[9,9,4],
                             [6,6,8],
                             [2,1,1]])
    a.longestIncreasingPath([[3,4,5],
                             [3,2,6],
                             [2,2,1]])