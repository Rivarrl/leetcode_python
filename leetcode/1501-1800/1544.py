# -*- coding: utf-8 -*-
# ======================================
# @File    : 1544.py
# @Time    : 2020/12/30 23:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1544. 整理字符串](https://leetcode-cn.com/problems/make-the-string-great/)
    """
    @timeit
    def makeGood(self, s: str) -> str:
        stk = []
        for i, c in enumerate(s):
            if stk and stk[-1] != c and stk[-1].lower() == c.lower():
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)

if __name__ == '__main__':
    a = Solution()
    a.makeGood(s = "leEeetcode")
    a.makeGood(s = "abBAcC")
    a.makeGood(s = "s")