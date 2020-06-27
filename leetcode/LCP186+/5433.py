# -*- coding: utf-8 -*-
# ======================================
# @File    : 5433.py
# @Time    : 2020/6/27 22:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5433. n 的第 k 个因子]()
    """
    @timeit
    def kthFactor(self, n: int, k: int) -> int:
        tot = 0
        for i in range(1, n + 1):
            if n % i == 0: tot += 1
            if tot == k: return i
        return -1

if __name__ == '__main__':
    a = Solution()
    a.kthFactor(n = 12, k = 3)
    a.kthFactor(n = 7, k = 2)
    a.kthFactor(n = 4, k = 4)
    a.kthFactor(n = 1, k = 1)
    a.kthFactor(n = 1000, k = 3)