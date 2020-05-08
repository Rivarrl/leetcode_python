# -*- coding: utf-8 -*-
# ======================================
# @File    : 537.py
# @Time    : 2020/5/9 2:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [537. 复数乘法](https://leetcode-cn.com/problems/complex-number-multiplication/)
    """
    @timeit
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def f(x):
            lx = x.split('+')
            lx[1] = lx[1][:-1]
            return [int(e) for e in lx]
        la, lb = f(a), f(b)
        s = la[0] * lb[0] - la[1] * lb[1]
        x = la[0] * lb[1] + la[1] * lb[0]
        return "{}+{}i".format(s, x)

if __name__ == '__main__':
    a = Solution()
    a.complexNumberMultiply("1+1i", "1+1i")
    a.complexNumberMultiply("1+-1i", "1+-1i")