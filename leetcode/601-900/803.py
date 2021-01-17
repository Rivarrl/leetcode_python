# -*- coding: utf-8 -*-
# ======================================
# @File    : 803.py
# @Time    : 2021/1/16 18:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [803. 打砖块](https://leetcode-cn.com/problems/bricks-falling-when-hit/)
    """
    @timeit
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
        n, m, l = len(grid), len(grid[0]), len(hits)
        for i, j in hits:
            grid[i][j] -= 1
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1) + 1
        def is_connected(i, j):
            if i == 0: return True
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == 2:
                    return True
            return False
        for j in range(m):
            dfs(0, j)
        res = [0] * l
        k = l - 1
        for i, j in hits[::-1]:
            grid[i][j] += 1
            if grid[i][j] == 1 and is_connected(i, j):
                res[k] = dfs(i, j) - 1
            k -= 1
        return res

    @timeit
    def hitBricks2(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        n, m, l = len(grid), len(grid[0]), len(hits)
        dsu = []
        for i, j in hits:
            grid[i][j] -= 1
        


if __name__ == '__main__':
    a = Solution()
    a.hitBricks(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]])
    a.hitBricks(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]])
    a.hitBricks([[1],[1],[1],[1],[1]], [[3,0],[4,0],[1,0],[2,0],[0,0]])