# -*- coding: utf-8 -*-
# ======================================
# @File    : 1162.py
# @Time    : 2019/11/27 14:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1162. 地图分析](https://leetcode-cn.com/problems/as-far-from-land-as-possible/)
    """
    @timeit
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        思路：暴力求解，记录每个点向右向下最长的边
        """
        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        stk = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    stk.append((i, j, 0))
                    vis[i][j] = 1
        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        res = -1
        while stk:
            i, j, step = stk.pop()
            if grid[i][j] == 0:
                res = max(res, step)
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and not vis[x][y]:
                    vis[x][y] = 1
                    stk.insert(0, (x, y, step+1))
        return res

if __name__ == '__main__':
    a = Solution()
    # a.maxDistance([[1,1,1],[1,0,1],[1,1,1]])
    # a.maxDistance([[1,1,0,0]])
    # a.maxDistance([[0]])
    # a.maxDistance([[1,1,0],[1,1,1],[1,1,1],[1,1,1]])
    # a.maxDistance([[0,0],[1,1]])
    a.maxDistance([[1,1,0,1,1,1,1,0],
                   [0,1,1,0,0,0,1,1],
                   [1,0,1,1,1,1,1,1],
                   [1,1,1,0,0,1,1,1],
                   [1,0,1,0,1,1,1,0],
                   [1,1,1,1,1,1,1,1],
                   [0,1,1,1,0,1,1,1],
                   [0,1,1,0,1,1,0,1]])