# -*- coding: utf-8 -*-
# ======================================
# @File    : 741.py
# @Time    : 2019/12/19 11:24
# @Author  : Rivarrl
# ======================================
import sys
print(sys.path)
from algorithm_utils import *

class Solution:
    """
    [741. 摘樱桃](https://leetcode-cn.com/problems/cherry-pickup/)
    """
    @timeit
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        可看成两个人同时从0，0点摘，走到n-1,n-1的时候最多可摘多少。
        """
        stk = [(0, 0, 0, 0)]
        N = len(grid)
        steps = N * 2 - 2
        vis = [set() for _ in range(steps)]
        vis[0].add((0, 0))
        dp = [0] * (steps)
        dxy = [[-1,0],[0,1],[1,0],[0,-1]]
        while stk:
            i1, i2, step, picked = stk.pop()
            j1, j2 = step - i1, step - i2
            if i1 == i2:
                picked += grid[i1][j1]
            else:
                picked += grid[i1][j1] + grid[i2][j2]
            dp[step] = max(dp[step], picked)
            for dx1, dy1 in dxy:
                x1, y1 = i1 + dx1, j1 + dy1
                if x1 < 0 or x1 == N or y1 < 0 or y2 == N: continue
                for dx2, dy2 in dxy:
                    x2, y2 = i2 + dx2, j2 + dy2
                    if x2 < 0 or x2 == N or y2 < 0 or y2 == N or grid[x1][x2] == -1 or (x1, x2) in vis[step+1]: continue
                    vis[step+1].add((x1, x2))
                    stk.insert(0, (x1, x2))




if __name__ == '__main__':
    a = Solution()
    a.cherryPickup([[0, 1, -1],
                    [1, 0, -1],
                    [1, 1,  1]])