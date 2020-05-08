# -*- coding: utf-8 -*-
# ======================================
# @File    : 69.py
# @Time    : 2020/5/9 0:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r - x > 0.01:
            r = (r*r + x) / (2 * r)
        return int(r)

if __name__ == '__main__':
    a = Solution()
    a.mySqrt(4)
    a.mySqrt(8)