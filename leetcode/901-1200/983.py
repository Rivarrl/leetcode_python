# -*- coding: utf-8 -*-
# ======================================
# @File    : 983.py
# @Time    : 2020/5/6 0:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [983. 最低票价](https://leetcode-cn.com/problems/minimum-cost-for-tickets/)
    """
    @timeit
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]
        days = set(days)
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            if not i in days:
                dp[i] = dp[i-1]
            else:
                dp7 = dp[i-7] if i >= 7 else 0
                dp30 = dp[i-30] if i >= 30 else 0
                dp[i] = min(dp[i-1] + costs[0], dp7 + costs[1], dp30 + costs[2])
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    a.mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15])
    a.mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15])