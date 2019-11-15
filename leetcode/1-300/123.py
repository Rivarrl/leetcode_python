# -*- coding: utf-8 -*-
# ======================================
# @File    : 123.py
# @Time    : 2019/11/15 11:42
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [123. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)
    """
    @timeit
    def maxProfit(self, prices: List[int]) -> int:
        """
        思路：动态规划，把持有和未持有作为两种状态10，由于本题可以买卖两次，再加一个次数的维度
        按持有次数把状态分为0次，1次，2次，0次是没有意义的
        dp[i][j][k] 表示第j次持有的时候在i时刻选择状态k持有1/未持有0
        其中按时间顺序，是dp[i][1][1]第一次买 -> dp[i][1][0]第一次卖 -> dp[i][2][1]第二次买 -> dp[i][2][0]第二次卖
        这四个关系是按时间影响后面结果的，所以k=2，有：
        dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
        dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
        注意顺序，每次先更改对本次没有影响的值
        最终return dp[n-1][2][0]即可，至于dp只与上一状态有关，可以用四个变量进行压缩
        """
        i20, i21, i10, i11 = 0, -float('inf'), 0, -float('inf')
        for x in prices:
            # 第二次卖
            i20 = max(i20, i21 + x)
            # 第二次买
            i21 = max(i21, i10 - x)
            # 第一次卖
            i10 = max(i10, i11 + x)
            # 第一次买
            i11 = max(i11, -x)
        return max(i20, i21)


if __name__ == '__main__':
    a = Solution()
    a.maxProfit([1,2,3,4,5])
    a.maxProfit([5,4,3,2,1])
    a.maxProfit([3,3,5,0,0,3,1,4])