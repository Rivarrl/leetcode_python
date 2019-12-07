# -*- coding: utf-8 -*-
# ======================================
# @File    : 1139.py
# @Time    : 2019/11/27 14:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1139. 最大的以 1 为边界的正方形](https://leetcode-cn.com/problems/largest-1-bordered-square/)
    """
    @timeit
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """
        思路：对每个1bfs
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
    a.largest1BorderedSquare([[1,0,1],[0,0,0],[1,0,1]])
    a.largest1BorderedSquare([[1,0,0],[0,0,0],[0,0,0]])