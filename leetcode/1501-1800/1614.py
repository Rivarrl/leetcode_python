# -*- coding: utf-8 -*-
# ======================================
# @File    : 1614.py
# @Time    : 2020/10/12 12:57 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1614. 括号的最大嵌套深度](https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses/)
    """
    @timeit
    def maxDepth(self, s: str) -> int:
        r = res = 0
        for c in s:
            if c == '(':
                r += 1
            elif c == ')':
                r -= 1
            res = max(res, r)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxDepth(s = "(1+(2*3)+((8)/4))+1")
    a.maxDepth(s = "(1)+((2))+(((3)))")
    a.maxDepth(s = "1+(2*3)/(2-1)")
    a.maxDepth(s = "1")