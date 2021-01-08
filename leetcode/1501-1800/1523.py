# -*- coding: utf-8 -*-
# ======================================
# @File    : 1523.py
# @Time    : 2021/1/8 23:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1523. 在区间范围内统计奇数数目](https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range/)
    """
    @timeit
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + high % 2 + low % 2) // 2

if __name__ == '__main__':
    a = Solution()
    a.countOdds(low = 3, high = 7)
    a.countOdds(low = 8, high = 10)
    a.countOdds(21, 22)