# -*- coding: utf-8 -*-
# ======================================
# @File    : 10-1.py
# @Time    : 2020/4/21 13:58
# @Author  : Rivarrl
# ======================================
# [面试题10- I. 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def fib(self, n: int) -> int:
        if n <= 1: return n
        res = pre = 0
        last = 1
        for i in range(2, n+1):
            res = last + pre
            pre, last = last, res
        return res % (10**9+7)

if __name__ == '__main__':
    a = Solution()
    a.fib(2)
    a.fib(5)
    a.fib(10)
    a.fib(45)