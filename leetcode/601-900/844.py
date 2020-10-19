# -*- coding: utf-8 -*-
# ======================================
# @File    : 844.py
# @Time    : 2020/10/19 12:47 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [844. 比较含退格的字符串](https://leetcode-cn.com/problems/backspace-string-compare/)
    """
    @timeit
    def backspaceCompare(self, S: str, T: str) -> bool:
        def f(S):
            stk = []
            for c in S:
                if c == "#":
                    if stk: stk.pop()
                else:
                    stk.append(c)
            return stk
        return f(S) == f(T)

if __name__ == '__main__':
    a = Solution()
    a.backspaceCompare(S = "ab#c", T = "ad#c")
    a.backspaceCompare(S = "ab##", T = "c#d#")
    a.backspaceCompare(S = "a##c", T = "#a#c")
    a.backspaceCompare(S = "a#c", T = "b")