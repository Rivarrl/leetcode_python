# -*- coding: utf-8 -*-
# ======================================
# @File    : 03-03.py
# @Time    : 2020/12/12 20:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class StackOfPlates:
    """
    [面试题 03.03. 堆盘子](https://leetcode-cn.com/problems/stack-of-plates-lcci/)
    """

    def __init__(self, cap: int):
        self.cap = cap
        self.stk = []

    def push(self, val: int) -> None:
        if not self.cap: return
        if not self.stk or len(self.stk[-1]) == self.cap:
            self.stk.append([val])
        else:
            self.stk[-1].append(val)

    def pop(self) -> int:
        res = -1
        if self.stk and self.stk[-1]:
            res = self.stk[-1].pop()
            if not self.stk[-1]: self.stk.pop()
        return res

    def popAt(self, index: int) -> int:
        res = -1
        if index < len(self.stk):
            res = self.stk[index].pop()
            if not self.stk[index]: self.stk.pop(index)
        return res

