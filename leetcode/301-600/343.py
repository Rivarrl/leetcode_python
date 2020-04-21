# -*- coding: utf-8 -*-
# ======================================
# @File    : 343.py
# @Time    : 2020/4/21 15:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [343. 整数拆分](https://leetcode-cn.com/problems/integer-break/)
    """
    def integerBreak(self, n: int) -> int:
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
    a.integerBreak(2)
    a.integerBreak(10)