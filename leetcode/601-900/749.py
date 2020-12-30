# -*- coding: utf-8 -*-
# ======================================
# @File    : 749.py
# @Time    : 2020/12/29 23:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [749. 隔离病毒](https://leetcode-cn.com/problems/contain-virus/)
    """
    @timeit
    def containVirus(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def f(i, j):
            if (i, j) not in seen:
                seen.add((i, j))
                regions[-1].add((i, j))
                for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ni < n and 0 <= nj < m:
                        if grid[ni][nj] == 1:
                            f(ni, nj)
                        elif grid[ni][nj] == 0:
                            infect[-1].add((ni, nj))
                            blocks[-1] += 1
        ans = 0
        while True:
            seen = set()
            regions = [] # 当前感染区域
            infect = [] # 下次感染扩散的block
            blocks = [] # 需要建墙的数量
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1 and (i, j) not in seen:
                        regions.append(set())
                        infect.append(set())
                        blocks.append(0)
                        f(i, j)
            if not regions: break
            rescue_idx = infect.index(max(infect, key=len))
            ans += blocks[rescue_idx]

            for i in range(len(regions)):
                if i == rescue_idx:
                    for x, y in regions[i]:
                        grid[x][y] = -1
                else:
                    for x, y in infect[i]:
                        grid[x][y] = 1
        return ans

if __name__ == '__main__':
    a = Solution()
    a.containVirus(grid =
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]])
    a.containVirus(grid =
[[1,1,1],
 [1,0,1],
 [1,1,1]])
    a.containVirus(grid =
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]])