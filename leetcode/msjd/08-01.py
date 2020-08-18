# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-01.py
# @Time    : 2020/8/17 17:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.01. 三步问题](https://leetcode-cn.com/problems/three-steps-problem-lcci/)
    """
    @timeit
    def waysToStep(self, n: int) -> int:
        x = [1, 2, 4]
        if n <= 3: return x[n-1]
        mod = 10 ** 9 + 7
        for i in range(3, n):
            x[0], x[1], x[2] = x[1], x[2], sum(x) % mod
        return x[-1]


if __name__ == '__main__':
    a = Solution()
    a.waysToStep(3)
    a.waysToStep(5)