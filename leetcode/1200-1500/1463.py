# -*- coding: utf-8 -*-
# ======================================
# @File    : 1463.py
# @Time    : 2020/6/1 20:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1463. 摘樱桃 II](https://leetcode-cn.com/problems/cherry-pickup-ii/)
    """
    @timeit
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = {(0,m-1): grid[0][0] + grid[0][m-1]}
        for i in range(1, n):
            dp2 = {}
            for y1, y2 in dp:
                for dy1 in range(-1, 2):
                    yy1 = y1 + dy1
                    if yy1 < 0 or yy1 >= m: continue
                    for dy2 in range(-1, 2):
                        yy2 = y2 + dy2
                        if yy2 < 0 or yy2 >= m: continue
                        c = grid[i][yy1] if yy1 == yy2 else grid[i][yy1] + grid[i][yy2]
                        dp2[(yy1, yy2)] = max(dp2.get((yy1, yy2), 0), dp[(y1, y2)] + c)
            dp = dp2
        return max(dp.values())

if __name__ == '__main__':
    a = Solution()
    a.cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
    a.cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])
    a.cherryPickup(grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]])
    a.cherryPickup(grid = [[1,1],[1,1]])