# -*- coding: utf-8 -*-
# ======================================
# @File    : 32.py
# @Time    : 2020/7/4 14:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)
    """
    @timeit
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stk, rec = [], [0] * n
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif stk:
                j = stk.pop()
                rec[j], rec[i] = 1, 1
        ans, m = 0, 0
        for i in rec:
            if i == 1:
                m += 1
            else:
                ans = max(m, ans)
                m = 0
        return max(m, ans)


if __name__ == '__main__':
    a = Solution()
    a.longestValidParentheses("(()")
    a.longestValidParentheses(")()())")