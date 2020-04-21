# -*- coding: utf-8 -*-
# ======================================
# @File    : 14-1.py
# @Time    : 2020/4/21 14:43
# @Author  : Rivarrl
# ======================================
# [面试题14- I. 剪绳子](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def cuttingRope(self, n: int) -> int:
        if n <= 2: return 1
        if n == 3: return 2
        base = 1
        if n % 3 == 1:
            base = 4
            n -= 3
        res = 3 ** (n // 3) * base
        if (n % 3) != 0:
            res *= (n % 3)
        return res

if __name__ == '__main__':
    a = Solution()
    a.cuttingRope(2)
    a.cuttingRope(5)
    a.cuttingRope(10)