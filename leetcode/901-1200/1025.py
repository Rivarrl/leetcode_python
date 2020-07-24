# -*- coding: utf-8 -*-
# ======================================
# @File    : 1025.py
# @Time    : 2020/7/24 9:53 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1025. 除数博弈](https://leetcode-cn.com/problems/divisor-game/)
    """
    @timeit
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


if __name__ == '__main__':
    a = Solution()
    a.divisorGame(2)
    a.divisorGame(3)