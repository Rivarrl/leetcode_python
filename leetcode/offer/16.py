# -*- coding: utf-8 -*-
# ======================================
# @File    : 16.py
# @Time    : 2020/4/21 16:11
# @Author  : Rivarrl
# ======================================
# [面试题16. 数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def myPow(self, x: float, n: int) -> float:
        # 快速幂
        if x == 0: return 0
        res = 1
        if n < 0:
            x = 1 / x
            n = -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.myPow(2.0000, 10)
    a.myPow(2.1000, 3)
    a.myPow(2.0000, -2)