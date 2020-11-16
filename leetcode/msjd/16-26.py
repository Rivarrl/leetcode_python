# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-26.py
# @Time    : 2020/11/16 1:51 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.26. 计算器](https://leetcode-cn.com/problems/calculator-lcci/)
    """
    @timeit
    def calculate(self, s: str) -> int:
        stk1, stk2 = [], []
        cur = ''
        for c in s:
            if c == ' ': continue
            if c.isdigit():
                cur += c
            else:
                x = int(cur)
                if stk2 and stk2[-1] in ("*", "/"):
                    op = stk2.pop()
                    y = stk1.pop()
                    if op == '*':
                        y *= x
                    else:
                        y //= x
                    x = y
                stk1.append(x)
                stk2.append(c)
                cur = ''
        x = int(cur)
        if not stk2: return x
        if stk2[-1] == '*':
            stk1[-1] *= x
            stk2.pop()
        elif stk2[-1] == '/':
            stk1[-1] //= x
            stk2.pop()
        else:
            stk1.append(x)
        res = stk1[0]
        for i in range(len(stk2)):
            if stk2[i] == '+':
                res += stk1[i+1]
            else:
                res -= stk1[i+1]
        return res

if __name__ == '__main__':
    a = Solution()
    a.calculate("3+2*2")
    a.calculate(" 3/2 ")
    a.calculate(" 3+5 / 2 ")
    a.calculate("1-1+1")