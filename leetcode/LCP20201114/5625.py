# -*- coding: utf-8 -*-
# ======================================
# @File    : 5625.py
# @Time    : 2020/12/13 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5625. 比赛中的配对次数]()
    """
    @timeit
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            res += (n >> 1)
            n = (n >> 1) + (n % 2)
        return res

if __name__ == '__main__':
    a = Solution()
    a.numberOfMatches(1)
    a.numberOfMatches(2)
    a.numberOfMatches(7)
    a.numberOfMatches(14)