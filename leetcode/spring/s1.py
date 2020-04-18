# -*- coding: utf-8 -*-
# ======================================
# @File    : s1.py
# @Time    : 2020/4/18 15:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minCount(self, coins: List[int]) -> int:
        res = 0
        for c in coins:
            res += c // 2 + c % 2
        return res


if __name__ == '__main__':
    a = Solution()
    a.minCount([4,2,1])
    a.minCount([2,3,10])