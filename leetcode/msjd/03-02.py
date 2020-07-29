# -*- coding: utf-8 -*-
# ======================================
# @File    : 03-02.py
# @Time    : 2020/7/30 0:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class MinStack:
    """
    [面试题 03.02. 栈的最小值](https://leetcode-cn.com/problems/min-stack-lcci/)
    """
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minstack) == 0 or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
