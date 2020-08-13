# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-05.py
# @Time    : 2020/8/13 23:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.05. 阶乘尾数](https://leetcode-cn.com/problems/factorial-zeros-lcci/)
    """
    @timeit
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            n //= 5
            res += n
        return res

if __name__ == '__main__':
    a = Solution()
    a.trailingZeroes(3)
    a.trailingZeroes(5)
    a.trailingZeroes(100)