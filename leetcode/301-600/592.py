# -*- coding: utf-8 -*-
# ======================================
# @File    : 592.py
# @Time    : 2020/12/16 9:41 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [592. 分数加减运算](https://leetcode-cn.com/problems/fraction-addition-and-subtraction/)
    """
    @timeit
    def fractionAddition(self, expression: str) -> str:
        expression += '+'
        sym = 1
        last = ''
        arr = []
        for c in expression:
            if c in {'+', '-'}:
                if last:
                    arr.append([sym, *[int(e) for e in last.split('/')]])
                last = ''
                sym = 1 if c == '+' else -1
            else:
                last += c
        def gcd(x, y):
            if y == 0: return x
            return gcd(y, x % y)
        def lcd(x, y):
            return x * y // gcd(x, y)
        x = 1
        for _, _, b in arr:
            x = lcd(b, x)
        res = 0
        for s, a, b in arr:
            res += s * (a * (x//b))
        q = gcd(abs(res), x)
        return '{}/{}'.format(str(res//q), x//q)


if __name__ == '__main__':
    a = Solution()
    a.fractionAddition("-1/2+1/2")
    a.fractionAddition("-1/2+1/2+1/3")
    a.fractionAddition("1/3-1/2")
    a.fractionAddition("5/3+1/3")