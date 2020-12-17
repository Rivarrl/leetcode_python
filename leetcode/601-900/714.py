# -*- coding: utf-8 -*-
# ======================================
# @File    : 714.py
# @Time    : 2020/12/17 0:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
    """
    @timeit
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp1 持有， dp0 未持有
        n = len(prices)
        if n <= 1: return 0
        dp1, dp0 = [0] * n, [0] * n
        dp1[0] = -prices[0]
        for i in range(1, n):
            dp0[i] = max(dp0[i-1], dp1[i-1] + prices[i] - fee)
            dp1[i] = max(dp1[i-1], dp0[i-1] - prices[i])
        return dp0[-1]

    @timeit
    def maxProfit2(self, prices: List[int], fee: int) -> int:
        # 贪心
        n = len(prices)
        if n <= 1: return 0
        res = 0
        cur = prices[0]
        for i in range(1, n):
            if prices[i] < cur:
                cur = prices[i]
            elif prices[i] > cur + fee:
                res += prices[i] - cur - fee
                cur = prices[i] - fee
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2)
