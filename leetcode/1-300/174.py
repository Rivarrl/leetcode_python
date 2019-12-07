# -*- coding: utf-8 -*-
# ======================================
# @File    : 174.py
# @Time    : 2019/11/25 11:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [174. 地下城游戏](https://leetcode-cn.com/problems/dungeon-game/)
    """
    @timeit
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        思路：动态规划
        """
        n = len(dungeon)
        m = len(dungeon[0])
        inf = 1 << 31
        dp = [[inf] * m for _ in range(n)]
        dp[-1][-1] = max(-dungeon[-1][-1], 0) + 1

        for i in range(n-2, -1, -1):
            dp[i][-1] = max(-dungeon[i][-1] + dp[i+1][-1], 1)
        for j in range(m-2, -1, -1):
            dp[-1][j] = max(-dungeon[-1][j] + dp[-1][j+1], 1)
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        return dp[0][0]


if __name__ == '__main__':
    a = Solution()
    a.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])