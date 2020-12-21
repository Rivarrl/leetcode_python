# -*- coding: utf-8 -*-
# ======================================
# @File    : 640.py
# @Time    : 2020/12/21 9:31 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [640. 求解方程](https://leetcode-cn.com/problems/solve-the-equation/)
    """
    @timeit
    def solveEquation(self, equation: str) -> str:
        s = z = 0
        k = ''
        sym = flag = 1
        equation += '+'
        for c in equation:
            if c.isdigit():
                k += c
            else:
                if c in {'=', '-', '+'}:
                    if k:
                        s += int(k) * sym * flag
                    if c == '=': sym = -1
                    flag = -1 if c == '-' else 1
                else:
                    if not k: k = '1'
                    z += int(k) * sym * flag
                k = ''
        if z == 0 and s == 0:
            return 'Infinite solutions'
        if z == 0:
            return 'No solution'
        if s == 0:
            return 'x=0'
        def gcd(x, y):
            if y == 0: return x
            return gcd(y, x % y)
        g = gcd(abs(z), abs(s))
        z //= g
        s //= g
        if z == 1:
            return 'x={}'.format(-s)
        if z == -1:
            return 'x={}'.format(s)
        if z < 0:
            return '{}x={}'.format(-z, s)
        return '{}x={}'.format(z, -s)


if __name__ == '__main__':
    a = Solution()
    a.solveEquation("x+5-3+x=6+x-2")
    a.solveEquation("x=x")
    a.solveEquation("2x=x")
    a.solveEquation("2x+3x-6x=x+2")
    a.solveEquation("x=x+2")