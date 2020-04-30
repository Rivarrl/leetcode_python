# -*- coding: utf-8 -*-
# ======================================
# @File    : 64.py
# @Time    : 2020/4/30 21:37
# @Author  : Rivarrl
# ======================================
# [面试题64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)
from algorithm_utils import *
class Solution:
    @timeit
    def sumNums(self, n: int) -> int:
        # 利用短路逻辑
        def f(x):
            return x and (x + f(x-1))
        return f(n)

if __name__ == '__main__':
    a = Solution()
    a.sumNums(3)