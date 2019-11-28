# -*- coding: utf-8 -*-
# ======================================
# @File    : 980.py
# @Time    : 2019/11/29 0:17
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [980. 不同路径 III](https://leetcode-cn.com/problems/unique-paths-iii/)
    """
    @timeit
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        思路：dfs，固定搜索深度为0的个数+1，不够的剪掉
        """
        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        st = None
        max_depth = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    st = i, j
                elif grid[i][j] == 0:
                    max_depth += 1

        dxy = ((0,1),(1,0),(0,-1),(-1,0))
        res = 0
        def dfs(i, j, depth):
            nonlocal res
            if grid[i][j] == 2 or depth == max_depth:
                if grid[i][j] == 2 and depth == max_depth:
                    res += 1
                return
            vis[i][j] = 1
            for dx, dy in dxy:
                x, y = i + dx, j + dy
                if x < 0 or x == n or y < 0 or y == m or grid[x][y] == -1 or vis[x][y]: continue
                dfs(x, y, depth+1)
            vis[i][j] = 0
        dfs(st[0], st[1], 0)
        return res


if __name__ == '__main__':
    a = Solution()
    a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    a.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
    a.uniquePathsIII([[0,1],[2,0]])