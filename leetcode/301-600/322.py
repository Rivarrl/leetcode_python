# -*- coding: utf-8 -*-
# ======================================
# @File    : 322.py
# @Time    : 2019/11/16 19:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [322. 零钱兑换](https://leetcode-cn.com/problems/coin-change)
    """
    @timeit
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        思路：背包问题
        """
        if amount == 0: return 0
        n = len(coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(n):
            wi = coins[i]
            if wi > amount: continue
            for j in range(amount - wi + 1):
                dp[j + wi] = min(dp[j + wi], dp[j] + 1)
        return -1 if dp[-1] == amount + 1 else dp[-1]


if __name__ == '__main__':
    a = Solution()
    a.coinChange([1,2,5], 11)
    a.coinChange([2], 4)