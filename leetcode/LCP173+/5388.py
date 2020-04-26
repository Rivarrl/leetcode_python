# -*- coding: utf-8 -*-
# ======================================
# @File    : 5388.py
# @Time    : 2020/4/19 11:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5388. 重新格式化字符串](https://leetcode-cn.com/problems/reformat-the-string/)
    """
    @timeit
    def reformat(self, s: str) -> str:
        d1, d2 = [], []
        for c in s:
            if c.isdigit():
                d1.append(c)
            else:
                d2.append(c)
        if abs(len(d1) - len(d2)) > 1: return ''
        if len(d1) < len(d2):
            d1, d2 = d2, d1
        res = ''
        for i in range(len(d2)):
            res += d1[i] + d2[i]
        if len(d1) > len(d2):
            res += d1[len(d2)]
        return res



if __name__ == '__main__':
    a = Solution()
    a.reformat(s = "a0b1c2")
    a.reformat(s = "leetcode")
    a.reformat(s = "1229857369")
    a.reformat(s = "covid2019")
    a.reformat(s = "ab123")