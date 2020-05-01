# -*- coding: utf-8 -*-
# ======================================
# @File    : 67.py
# @Time    : 2020/5/1 21:00
# @Author  : Rivarrl
# ======================================
# [面试题67. 把字符串转换成整数](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def strToInt(self, str: str) -> int:
        trans_table = [[0,1,2,3],
                       [3,3,2,3],
                       [3,3,2,3],
                       [3,3,3,3]]
        def f(x):
            if x == ' ': return 0
            elif x in '+-': return 1
            elif x in '0123456789': return 2
            else: return 3
        sta = 0
        sign, res = 1, 0
        for x in str:
            sta = trans_table[sta][f(x)]
            if sta == 1:
                sign = 1 if x == '+' else -1
            elif sta == 2:
                res = res * 10 + int(x)
            elif sta == 3:
                break
        return max(-(1<<31), min((1<<31) - 1, sign * res))

if __name__ == '__main__':
    a = Solution()
    a.strToInt("42")
    a.strToInt("    -42")
    a.strToInt("4193 with words")
    a.strToInt("words and 987")
    a.strToInt("-91283472332")