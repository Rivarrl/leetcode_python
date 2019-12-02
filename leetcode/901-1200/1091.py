# -*- coding: utf-8 -*-
# ======================================
# @File    : 1091.py
# @Time    : 2019/12/2 9:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1091. 二进制矩阵中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/)
    """
    @timeit
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        bfs
        """
        n, m = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        vis = {(0, 0): 1}
        stk = [(0, 0, 1)]
        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
        while stk:
            i, j, k = stk.pop()
            if i == n-1 and j == m-1: return k
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and not (x, y) in vis and grid[x][y] == 0:
                    vis[(x, y)] = k+1
                    stk.insert(0, (x, y, k+1))
        return -1


    @timeit
    def shortestPathBinaryMatrix2(self, grid: List[List[int]]) -> int:
        """
        双向bfs
        双向bfs要领：从起点和终点分别开始，双向交替步进，第一次访问到在另一个访问点集中出现的点停止搜索。
        """
        n, m = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        vis_head, vis_tail = {(0, 0): 1}, {(n-1, m-1): 1}
        stk_head, stk_tail = [(0, 0, 1)], [(n-1, m-1, 1)]
        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
        def bfs(stk, vis, vis_other):
            nstk = []
            while stk:
                i, j, k = stk.pop()
                if (i, j) in vis_other: return k + vis_other[(i, j)] - 1
                for dx, dy in dxy:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and not (x, y) in vis and grid[x][y] == 0:
                        vis[(x, y)] = k + 1
                        nstk.insert(0, (x, y, k+1))
            stk += nstk[:]
        while stk_head and stk_tail:
            r = bfs(stk_head, vis_head, vis_tail)
            if r: return r
            r = bfs(stk_tail, vis_tail, vis_head)
            if r: return r
        return -1

if __name__ == '__main__':
    a = Solution()
    a.shortestPathBinaryMatrix2([[0,1],[1,0]])
    a.shortestPathBinaryMatrix2([[0,0,0],[1,1,0],[1,1,0]])
    a.shortestPathBinaryMatrix2([[0,0,0,0,0,0,1],
                                [1,1,1,1,1,1,0],
                                [0,0,1,1,1,1,0],
                                [0,1,0,1,0,1,0],
                                [0,1,1,0,1,0,0],
                                [0,1,1,1,1,1,1],
                                [0,0,0,0,0,0,0]])

