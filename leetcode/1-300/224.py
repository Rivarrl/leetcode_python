# -*- coding: utf-8 -*-
# ======================================
# @File    : 224
# @Time    : 2021/3/10 12:57
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [224. 基本计算器](https://leetcode-cn.com/problems/basic-calculator/)
    """
    @timeit
    def calculate(self, s: str) -> int:
        stk = [1]
        i = 0
        n = len(s)
        d = 1
        res = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '(':
                stk.append(d)
                i += 1
            elif s[i] == ')':
                stk.pop()
                i += 1
            elif s[i] == '+':
                d = stk[-1]
                i += 1
            elif s[i] == '-':
                d = -stk[-1]
                i += 1
            else:
                t = 0
                while i < n and s[i] not in {' ', '(', ')', '+', '-'}:
                    t = t * 10 + int(s[i])
                    i += 1
                res += d * t
        return res

if __name__ == '__main__':
    a = Solution()
    a.calculate(s = "1 + 1")
    a.calculate(s = " 2-1 + 2 ")
    a.calculate(s = "(1+(4+5+2)-3)+(6+8)")