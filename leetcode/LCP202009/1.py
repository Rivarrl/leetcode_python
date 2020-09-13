# -*- coding: utf-8 -*-
# ======================================
# @File    : 1.py
# @Time    : 2020/9/12 15:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def calculate(self, s: str) -> int:
        A = lambda x, y: (2*x+y, y)
        B = lambda x, y: (x, 2*y+x)
        d = {"A":A, "B":B}
        x, y = 1, 0
        for op in s:
            x, y = d[op](x, y)
        return x + y

if __name__ == '__main__':
    a = Solution()
    a.calculate("AB")