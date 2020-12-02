# -*- coding: utf-8 -*-
# ======================================
# @File    : 1672.py
# @Time    : 2020/12/2 2:04 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1672. 最富有客户的资产总量](https://leetcode-cn.com/problems/richest-customer-wealth/)
    """
    @timeit
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)

if __name__ == '__main__':
    a = Solution()
    a.maximumWealth(accounts = [[1,2,3],[3,2,1]])
    a.maximumWealth(accounts = [[1,5],[7,3],[3,5]])
    a.maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]])