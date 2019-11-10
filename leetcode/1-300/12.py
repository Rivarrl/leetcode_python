# -*- coding: utf-8 -*-
# ======================================
# @File    : 12.py
# @Time    : 2019/11/10 23:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        [12. 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/)
        思路：字典表从高到低依次减
        """
        rmd = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
               9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for k, v in rmd.items():
            while num >= k:
                res += v
                num -= k
        return res