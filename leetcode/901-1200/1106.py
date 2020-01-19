# -*- coding: utf-8 -*-
# ======================================
# @File    : 1106
# @Time    : 2020/1/7 0:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1106. 解析布尔表达式](https://leetcode-cn.com/problems/parsing-a-boolean-expression/)
    """
    @timeit
    def parseBoolExpr(self, expression: str) -> bool:
        def op(o, a, r):
            if o == '|':
                return r or a
            elif o == '&':
                return r and a
            elif o == '!':
                return not r
            else:
                return r
        def dfs(k, o=''):
            res = None
            i = k
            while i < len(expression):
                if expression[i] in {'!', '|', '&'}:
                    inner, j = dfs(i+1, expression[i])
                    res = inner if res == None else res
                    res = op(o, inner, res)
                    i = j
                elif expression[i] == ')':
                    return res, i
                elif expression[i] in {'t', 'f'}:
                    if res == None:
                        res = True if expression[i] == 't' else False
                    if expression[i] == 't':
                        res = op(o, True, res)
                    else:
                        res = op(o, False, res)
                i += 1
            return res
        return dfs(0)


if __name__ == '__main__':
    a = Solution()
    # a.parseBoolExpr("!(f)")
    # a.parseBoolExpr("|(f,t)")
    # a.parseBoolExpr("&(t,f)")
    # a.parseBoolExpr("|(&(t,f,t),!(t))")
    # a.parseBoolExpr("&(t,t,t)")
    # a.parseBoolExpr("!(f)")
    # a.parseBoolExpr("!(&(!(t),&(f),|(f)))")
    a.parseBoolExpr("|(f,&(t,t))")