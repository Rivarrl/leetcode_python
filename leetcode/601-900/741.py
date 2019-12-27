# -*- coding: utf-8 -*-
# ======================================
# @File    : 741.py
# @Time    : 2019/12/19 11:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [741. 摘樱桃](https://leetcode-cn.com/problems/cherry-pickup/)
    """
    @timeit
    def cherryPickup3(self, grid: List[List[int]]) -> int:
        """
        可看成两个人同时从0，0点摘，走到n-1,n-1的时候最多可摘多少，自顶向下。
        """
        from functools import lru_cache
        @lru_cache(None)
        def dp(x1, x2, k):
            y1, y2 = k - x1, k - x2
            if x1 == x2 == k == 0: return grid[0][0]
            if any(e < 0 for e in {x1, x2, y1, y2}): return -1
            if grid[x1][y1] == -1 or grid[x2][y2] == -1: return -1
            m = max(dp(x1-1, x2, k-1), dp(x1, x2-1, k-1), dp(x1-1, x2-1, k-1), dp(x1, x2, k-1))
            if m < 0: return -1
            return m + grid[x1][y1] if x1 == x2 else m + grid[x1][y1] + grid[x2][y2]

        N = len(grid)
        return max(0, dp(N-1, N-1, (N-1) << 1))


    @timeit
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        自底向上
        """
        N = len(grid)
        dp = [[-1] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        for k in range(1, (N << 1) - 1):
            dp2 = [[-1] * N for _ in range(N)]
            for x1 in range(max(0, k - N + 1), min(k+1, N)):
                y1 = k - x1
                if grid[x1][y1] == -1: continue
                for x2 in range(max(0, k - N + 1), min(k+1, N)):
                    y2 = k - x2
                    if grid[x2][y2] == -1: continue
                    cur = max(dp[xi][xj] for xi in (x1, x1-1) for xj in (x2, x2-1) if x1 >= 0 and xj >= 0)
                    if cur >= 0:
                        cur += grid[x1][y1]
                        if x1 != x2: cur += grid[x2][y2]
                    dp2[x1][x2] = cur
            dp = dp2[:]
        return max(0, dp[-1][-1])


if __name__ == '__main__':
    a = Solution()
    a.cherryPickup([[1,1,-1],
                    [1,-1,1],
                    [-1,1,1]])
    a.cherryPickup([[0, 1, -1],
                    [1, 0, -1],
                    [1, 1,  1]])
    a.cherryPickup([[0, 1,1 ,0,0],
                    [1, 1,1 ,1,0],
                    [-1,1,1 ,1,-1],
                    [0, 1,1 ,1,0],
                    [1, 0,-1,0,0]])

    a.cherryPickup([[1,1,1,1,0,0,0],
                    [0,0,0,1,0,0,0],
                    [0,0,0,1,0,0,1],
                    [1,0,0,1,0,0,0],
                    [0,0,0,1,0,0,0],
                    [0,0,0,1,0,0,0],
                    [0,0,0,1,1,1,1]])

    a.cherryPickup([[1,-1,1,-1,1,1,1,1,1,-1],
                    [-1,1,1,-1,-1,1,1,1,1,1],
                    [1,1,1,-1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1],
                    [-1,1,1,1,1,1,1,1,1,1],
                    [1,-1,1,1,1,1,-1,1,1,1],
                    [1,1,1,-1,1,1,-1,1,1,1],
                    [1,-1,1,-1,-1,1,1,1,1,1],
                    [1,1,-1,-1,1,1,1,-1,1,-1],
                    [1,1,-1,1,1,1,1,1,1,1]])