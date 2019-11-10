# -*- coding: utf-8 -*-
# ======================================
# @File    : 13.py
# @Time    : 2019/11/10 23:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)
        思路：用字典先把题目说的表打上，通过观察可知，罗马数字是从高到低的顺序排列的，如果出现较小的数在较大的数之前的情况，例如IV，IX，CD，就用后一位的值减去当前位的值
        """
        rmd = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        i, l = 0, len(s)
        while i < l:
            if i < l - 1 and rmd[s[i]] < rmd[s[i+1]]:
                res += rmd[s[i+1]] - rmd[s[i]]
                i += 1
            else:
                res += rmd[s[i]]
            i += 1
        return res