# -*- coding: utf-8 -*-
# ======================================
# @File    : 5627.py
# @Time    : 2020/12/13 10:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import sys
sys.setrecursionlimit(3000)

class Solution:
    """
    [5627. 石子游戏 VII]()
    """
    @timeit
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        pre = [0]
        for x in stones:
            pre.append(pre[-1] + x)
        dp = [[-1] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 0
            for j in range(i+1, n):
                dp[i][j] = max(dp[i][j], pre[j] - pre[i] - dp[i][j-1], pre[j+1] - pre[i+1] - dp[i+1][j])
        return dp[0][n-1]

if __name__ == '__main__':
    a = Solution()
    a.stoneGameVII(stones = [5,3,1,4,2])
    a.stoneGameVII(stones = [7,90,5,1,100,10,10,2])
    import random
    x = [random.randint(1, 1000) for _ in range(1000)]
    print(x)
    a.stoneGameVII(x)