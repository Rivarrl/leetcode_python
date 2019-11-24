# -*- coding: utf-8 -*-
# ======================================
# @File    : 5272.py
# @Time    : 2019/11/24 10:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5272. 统计参与通信的服务器
    """
    @timeit
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = [[0] * m for _ in range(n)]
        for i in range(n):
            ctr = 0
            for j in range(m):
                if grid[i][j] != 0:
                    ctr += 1
                if ctr == 2: break
            if ctr == 2:
                for j in range(m):
                    if grid[i][j] != 0:
                        vis[i][j] = 1
        for j in range(m):
            ctr = 0
            for i in range(n):
                if grid[i][j] != 0:
                    ctr += 1
                    if ctr == 2: break
            if ctr == 2:
                for i in range(n):
                    if grid[i][j] != 0:
                        vis[i][j] = 1
        return sum(sum(e) for e in vis)

if __name__ == '__main__':
    a = Solution()
    a.countServers([[1,0],[0,1]])
    a.countServers([[1,0],[1,1]])
    a.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])