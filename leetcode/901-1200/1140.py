# -*- coding: utf-8 -*-
# ======================================
# @File    : 1140.py
# @Time    : 2019/11/27 14:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1140. 石子游戏 II](https://leetcode-cn.com/problems/stone-game-ii/)
    """
    @timeit
    def stoneGameII(self, piles: List[int]) -> int:
        """
        思路：动态规划，dp[i][j]表示当前M=j时，在piles[i:]中选择的最优解
        """
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if n - i <= 2 * j: return suf[i]
            res = pre = 0
            for x in range(2*j):
                if i + x == n: break
                pre += piles[i+x]
                cur = pre + suf[i+x+1] - dp(i+x+1, max(x+1, j))
                res = max(res, cur)
            memo[(i, j)] = res
            return res
        n = len(piles)
        suf = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suf[i] += suf[i+1] + piles[i]
        memo = {}
        return dp(0, 1)

if __name__ == '__main__':
    a = Solution()
    a.stoneGameII([2,7,9,4,4])
    a.stoneGameII([8,9,5,4,5,4,1,1,9,3,1,10,5,9,6,2,7,6,6,9])
