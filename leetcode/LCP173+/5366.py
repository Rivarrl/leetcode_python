# -*- coding: utf-8 -*-
# ======================================
# @File    : 5366.py
# @Time    : 2020/3/22 10:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5366. 检查网格中是否存在有效路径](https://leetcode-cn.com/problems/check-if-there-is-a-valid-path-in-a-grid/)
    """
    @timeit
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        st = (None, (0,2), (1,3), (2,3), (0,3), (1,2), (0,1))
        d = (None, ((0,1), (0,-1)), ((1,0), (-1,0)), ((0,-1),(1,0)), ((0, 1), (1, 0)), ((-1, 0),(0, -1)), ((-1, 0), (0, 1)))
        left, right, up, down = (0, -1), (0, 1), (-1, 0), (1, 0)
        n, m = len(grid), len(grid[0])
        stk = [(0, 0)]
        vis = [[0] * m for _ in range(n)]
        vis[0][0] = 1
        def ok(nxt, dx, dy):
            dxy = (dx, dy)
            if dxy == left:
                return 0 in nxt
            elif dxy == right:
                return 2 in nxt
            elif dxy == up:
                return 3 in nxt
            else:
                return 1 in nxt
        while stk:
            i, j = stk.pop(0)
            if i == n-1 and j == m-1:
                return True
            s = grid[i][j]
            for k in range(2):
                dx, dy = d[s][k]
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and vis[x][y] == 0 and ok(st[grid[x][y]], dx, dy):
                    stk.append((x, y))
                    vis[x][y] = 1
        return False


if __name__ == '__main__':
    a = Solution()
    a.hasValidPath(grid = [[2,4,3],[6,5,2]])
    a.hasValidPath(grid = [[1,2,1],[1,2,1]])
    a.hasValidPath(grid = [[1,1,2]])
    a.hasValidPath(grid = [[1,1,1,1,1,1,3]])
    a.hasValidPath(grid = [[2],[2],[2],[2],[2],[2],[6]])