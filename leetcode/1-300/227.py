# -*- coding: utf-8 -*-
# ======================================
# @File    : 227
# @Time    : 2021/3/11 9:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [227. 基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii/)
    """
    @timeit
    def calculate(self, s: str) -> int:
        i, n = 0, len(s)
        stk = [0]
        t = 0
        d = '+'
        for i in range(n):
            if s[i].isdigit():
                t = t * 10 + int(s[i])
            if i == n-1 or s[i] in {'+','-','*','/'}:
                if d == '+':
                    stk.append(t)
                elif d == '-':
                    stk.append(-t)
                elif d == '*':
                    stk[-1] *= t
                else:
                    ss = abs(stk[-1])
                    stk[-1] = 0 if ss == 0 else (stk[-1]//ss) * (ss // t)
                d = s[i]
                t = 0
        return sum(stk)


if __name__ == '__main__':
    a = Solution()
    a.calculate(s = "3+2*2")
    a.calculate(s = " 3/2 ")
    a.calculate(s = " 3+5 / 2 ")
    a.calculate("14-3/2")