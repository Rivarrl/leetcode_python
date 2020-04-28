# -*- coding: utf-8 -*-
# ======================================
# @File    : 20.py
# @Time    : 2020/4/28 15:13
# @Author  : Rivarrl
# ======================================
# [面试题20. 表示数值的字符串](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)
from algorithm_utils import *
class Solution:
    @timeit
    def isNumber(self, s: str) -> bool:
        trans_table = [[ 1,-1, 2, 4, 0,-1],
                       [-1,-1, 2, 4,-1,-1],
                       [-1, 6, 2, 3, 9,-1],
                       [-1, 6, 3,-1, 9,-1],
                       [-1,-1, 5,-1,-1,-1],
                       [-1, 6, 5,-1, 9,-1],
                       [ 8,-1, 7,-1,-1,-1],
                       [-1,-1, 7,-1, 9,-1],
                       [-1,-1, 7,-1,-1,-1],
                       [-1,-1,-1,-1, 9,-1]]
        def f(c):
            if c in ('+', '-'): return 0
            elif c == 'e': return 1
            elif c in '0123456789': return 2
            elif c == '.': return 3
            elif c == ' ': return 4
            else: return 5
        sta = 0
        for c in s:
            sta = trans_table[sta][f(c)]
            if sta == -1: return False
        return sta in {2,3,5,7,9}

if __name__ == '__main__':
    a = Solution()
    a.isNumber("+100")
    a.isNumber("5e2")
    a.isNumber("-123")
    a.isNumber("3.1416")
    a.isNumber("0123")
    a.isNumber("12e")
    a.isNumber("1a3.14")
    a.isNumber("1.2.3")
    a.isNumber("+-5")
    a.isNumber("-1E-16")
    a.isNumber("12e+5.4")
    a.isNumber(".20")
    a.isNumber(".2e81")