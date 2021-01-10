# -*- coding: utf-8 -*-
# ======================================
# @File    : 5633.py
# @Time    : 2021/1/9 22:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5633. 计算力扣银行的钱]()
    """
    @timeit
    def totalMoney(self, n: int) -> int:
        m, k = n // 7, n % 7
        h = m * 28 + 7 * (m * (m - 1) // 2)
        t = m * k + (1 + k) * k // 2
        return h + t

if __name__ == '__main__':
    a = Solution()
    a.totalMoney(n = 4)
    a.totalMoney(n = 10)
    a.totalMoney(n = 20)