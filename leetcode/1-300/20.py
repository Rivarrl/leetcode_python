# -*- coding: utf-8 -*-
# ======================================
# @File    : 20.py
# @Time    : 2020/8/8 23:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)
    """
    @timeit
    def isValid(self, s: str) -> bool:
        stk = []
        d = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in {'(', '[', '{'}:
                stk.append(c)
            else:
                if not stk or stk.pop() != d[c]:
                    return False
        return len(stk) == 0

if __name__ == '__main__':
    a = Solution()
    a.isValid("()")
    a.isValid("()[]{}")
    a.isValid("(]")
    a.isValid("([)]")
    a.isValid("{[]}")