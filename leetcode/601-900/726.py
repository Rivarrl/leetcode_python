# -*- coding: utf-8 -*-
# ======================================
# @File    : 726.py
# @Time    : 2020/12/25 1:31 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [726. 原子的数量](https://leetcode-cn.com/problems/number-of-atoms/)
    """
    @timeit
    def countOfAtoms(self, formula: str) -> str:
        from collections import defaultdict
        stk = []
        n = len(formula)
        i = 0
        rd = defaultdict(int)
        while i < n:
            if formula[i].isupper():
                j = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                x = formula[j:i]
                j = i
                while i < n and formula[i].isnumeric():
                    i += 1
                if i == j:
                    c = 1
                else:
                    c = int(formula[j:i])
                if stk:
                    stk[-1][x] += c
                else:
                    rd[x] += c
            elif formula[i] == '(':
                stk.append(defaultdict(int))
                i += 1
            else:
                i += 1
                j = i
                while i < n and formula[i].isnumeric():
                    i += 1
                if i == j:
                    c = 1
                else:
                    c = int(formula[j:i])
                cd = stk.pop()
                for k, v in cd.items():
                    if stk:
                        stk[-1][k] += c * v
                    else:
                        rd[k] += c * v
        return ''.join(['{}{}'.format(k, rd[k]) if rd[k] > 1 else k for k in sorted(rd.keys())])


if __name__ == '__main__':
    a = Solution()
    # a.countOfAtoms(formula = "H2O")
    # a.countOfAtoms(formula = "Mg(OH)2")
    # a.countOfAtoms(formula = "K4(ON(SO3)2)2")
    a.countOfAtoms("(NB3)33")