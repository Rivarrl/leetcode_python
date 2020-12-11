# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-09.py
# @Time    : 2020/12/11 1:07 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.09. 括号](https://leetcode-cn.com/problems/bracket-lcci/)
    """
    @timeit
    def generateParenthesis(self, n: int) -> List[str]:
        # 递归
        brackets = "()"
        def f(n):
            if n == 1: return [brackets]
            res = set()
            for x in f(n-1):
                m = (n-1) * 2
                for i in range(0, m+1):
                    res.add(x[:i] + brackets + x[i:])
            return list(res)
        return f(n)

    @timeit
    def generateParenthesis2(self, n: int) -> List[str]:
        # 回溯
        res = []
        def f(l, r, s):
            if l == n and r == n:
                res.append(s)
                return
            if l < r: return
            if l < n:
                f(l + 1, r, s + '(')
            if r < n:
                f(l, r + 1, s + ')')
        f(0,0,'')
        return res

if __name__ == '__main__':
    a = Solution()
    a.generateParenthesis(3)
    a.generateParenthesis2(3)