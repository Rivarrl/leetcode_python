# -*- coding: utf-8 -*-
# ======================================
# @File    : 5326.py
# @Time    : 2020/2/23 12:29
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5326. 有效的快递序列数目](https://leetcode-cn.com/problems/count-all-valid-pickup-and-delivery-options/)
    """
    @timeit
    def countOrders(self, n: int) -> int:
        # 排列组合
        mod = 10 ** 9 + 7
        if n == 1: return 1
        if n == 2: return 6
        dp = 6
        for i in range(2, n+1):
            dp = dp * ((2*i+1)*(2*i+2)//2 % mod) % mod
        return dp

if __name__ == '__main__':
    a = Solution()
    a.countOrders(3)