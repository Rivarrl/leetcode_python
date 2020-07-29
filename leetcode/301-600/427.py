# -*- coding: utf-8 -*-
# ======================================
# @File    : 427.py
# @Time    : 2020/7/29 9:57 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    """
    [427. 建立四叉树](https://leetcode-cn.com/problems/construct-quad-tree/)
    """
    @timeit
    def construct(self, grid: List[List[int]]) -> 'Node':
        def ok(i, j, s):
            return sum(grid[i+x][j+y] for x in range(s) for y in range(s)) in {0, s*s}
        def f(i, j, s):
            if s == 1 or ok(i, j, s): return Node(grid[i][j], True, None, None, None, None)
            t = s // 2
            NW, NE, SW, SE = f(i, j, t), f(i, j+t, t), f(i+t, j, t), f(i+t, j+t, t)
            return Node(1, False, NW, NE, SW, SE)
        n = len(grid)
        return f(0, 0, n)

if __name__ == '__main__':
    a = Solution()
    grid = [[1, 1, 1, 1, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 0, 0]]
