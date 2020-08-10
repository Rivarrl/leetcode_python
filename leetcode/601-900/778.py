# -*- coding: utf-8 -*-
# ======================================
# @File    : 778.py
# @Time    : 2020/8/10 21:27
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [778. 水位上升的泳池中游泳](https://leetcode-cn.com/problems/swim-in-rising-water/)
    """
    @timeit
    def swimInWater(self, grid: List[List[int]]) -> int:
        # bfs+优先队列
        import heapq
        stk = []
        heapq.heappush(stk, (grid[0][0], 0, 0))
        n = len(grid)
        seen = [[False] * n for _ in range(n)]
        seen[0][0] = True
        res = grid[-1][-1]
        while stk:
            s, i, j = heapq.heappop(stk)
            res = max(res, s)
            if i == j == n - 1: return res
            for dx, dy in ((0, -1), (1, 0), (-1, 0), (0, 1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n and not seen[x][y]:
                    seen[x][y] = True
                    heapq.heappush(stk, (grid[x][y], x, y))
        return -1

    @timeit
    def swimInWater2(self, grid: List[List[int]]) -> int:
        # 二分答案 + dfs judge
        def judge(x):
            stk = [(0, 0)]
            seen = [0] * n
            seen[0] = 1
            while stk:
                i, j = stk.pop()
                if i == j == n - 1: return True
                for ni, nj in ((i, j-1), (i+1, j), (i-1, j), (i, j+1)):
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] <= x and (seen[ni] >> nj) & 1 == 0:
                        seen[ni] |= (1 << nj)
                        stk.append((ni, nj))
            return False
        n = len(grid)
        lo, hi = grid[0][0], n*n-1
        while lo < hi:
            mi = lo + hi >> 1
            if judge(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo

if __name__ == '__main__':
    a = Solution()
    # a.swimInWater2([[0,2],[1,3]])
    # a.swimInWater2([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])
    a.swimInWater2([[3,2],[0,1]])