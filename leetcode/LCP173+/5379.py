# -*- coding: utf-8 -*-
# ======================================
# @File    : 5379.py
# @Time    : 2020/4/5 10:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5379. 石子游戏 III]()
    """
    @timeit
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * n
        dp[-1] = stoneValue[-1]
        for i in range(n-2, -1, -1):
            if i == n-2:
                dp[i] = max(stoneValue[i]-dp[i+1], stoneValue[i]+stoneValue[i+1])
            elif i == n-3:
                dp[i] = max(stoneValue[i]-dp[i+1], stoneValue[i]+stoneValue[i+1]-dp[i+2], stoneValue[i]+stoneValue[i+1]+stoneValue[i+2])
            else:
                dp[i] = max(stoneValue[i]-dp[i+1], stoneValue[i]+stoneValue[i+1]-dp[i+2], stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]-dp[i+3])
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

if __name__ == '__main__':
    a = Solution()
    a.stoneGameIII([1,2,3,7])
    a.stoneGameIII([1,2,3,-9])
    a.stoneGameIII([1,2,3,6])
    a.stoneGameIII([1,2,3,-1,-2,-3,7])
    a.stoneGameIII([-1,-2,-3])