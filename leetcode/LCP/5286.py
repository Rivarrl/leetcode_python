# -*- coding: utf-8 -*-
# ======================================
# @File    : 5286.py
# @Time    : 2019/12/15 10:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5286. 网格中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)
    """
    @timeit
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        ctr = sum(grid[i].count(1) for i in range(n))
        if ctr <= k: return n + m - 2
        if grid[n-1][m-1] == 1:
            k -= 1
            grid[n-1][m-1] = 0
        vis = [[[0] * m for _ in range(n)] for _ in range(k+1)]
        stk = [(0, 0, 0, 0)]
        dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        vis[0][0][0] = 1
        while stk:
            i, j, p, step = stk.pop()
            if i == n-1 and j == m-1: return step
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and vis[p][x][y] == 0:
                    vis[p][x][y] = 1
                    if grid[x][y] == 0: stk.insert(0, (x, y, p, step+1))
                    elif p < k: stk.insert(0, (x, y, p+1, step+1))
        return -1


if __name__ == '__main__':
    a = Solution()
    a.shortestPath(grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1)
    a.shortestPath(grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1)
