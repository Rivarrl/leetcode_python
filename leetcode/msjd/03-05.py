# -*- coding: utf-8 -*-
# ======================================
# @File    : 03-05.py
# @Time    : 2020/12/12 21:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class SortedStack:
    """
    [面试题 03.05. 栈排序](https://leetcode-cn.com/problems/sort-of-stacks-lcci/)
    """
    def __init__(self):
        self.stk = []
        self.tmp = []

    def push(self, val: int) -> None:
        while self.stk and self.stk[-1] < val:
            self.tmp.append(self.stk.pop())
        while self.tmp and self.tmp[-1] > val:
            self.stk.append(self.tmp.pop())
        self.stk.append(val)

    def pop(self) -> None:
        while self.tmp:
            self.stk.append(self.tmp.pop())
        if not self.stk: return
        return self.stk.pop()

    def peek(self) -> int:
        if not self.stk and not self.tmp: return -1
        return self.tmp[0] if self.tmp else self.stk[-1]

    def isEmpty(self) -> bool:
        return len(self.stk) + len(self.tmp) == 0
