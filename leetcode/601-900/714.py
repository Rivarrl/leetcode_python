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