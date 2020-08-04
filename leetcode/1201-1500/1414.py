# -*- coding: utf-8 -*-
# ======================================
# @File    : 1414.py
# @Time    : 2020/4/24 13:08
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1414. 和为 K 的最少斐波那契数字数目](https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)
    """
    @timeit
    def findMinFibonacciNumbers(self, k: int) -> int:
        x, y, z = 1, 1, 1
        s = list()
        s.append(1)
        while z < k:
            z = x + y
            x, y = y, z
            s.append(z)
        res = 0
        for x in s[::-1]:
            if k >= x:
                k -= x
                res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.findMinFibonacciNumbers(7)
    a.findMinFibonacciNumbers(10)
    a.findMinFibonacciNumbers(19)