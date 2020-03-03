# -*- coding: utf-8 -*-
# ======================================
# @File    : 994.py
# @Time    : 2020/03/04 00:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [994. 腐烂的橘子](https://leetcode-cn.com/problems/rotting-oranges/)
    bfs记录步数，把被传染的橘子状态值改为1，最后判断是否有新鲜橘子
    """
    @timeit
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stk = []
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    stk.append((i, j, 0))
        dxy = ((0, 1), (0, -1), (-1, 0), (1, 0))
        st = 0
        while stk:
            i, j, s = stk.pop(0)
            st = max(st, s)
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                    grid[x][y] = 2
                    stk.append((x, y, s+1))
        def ok(arr):
            for row in arr:
                for e in row:
                    if e == 1: return False
            return True
        return st if ok(grid) else -1


if __name__ == '__main__':
    a = Solution()
    a.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    a.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
    a.orangesRotting([[0,2]])