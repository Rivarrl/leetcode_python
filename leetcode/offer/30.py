# -*- coding: utf-8 -*-
# ======================================
# @File    : 30.py
# @Time    : 2020/5/7 15:08
# @Author  : Rivarrl
# ======================================
# [面试题30. 包含min函数的栈](https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof)

class MinStack:
    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        self.min_stk.append(self.min_stk[-1] if self.min_stk and self.min_stk[-1] < x else x)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def min(self) -> int:
        return self.min_stk[-1]

if __name__ == '__main__':
    a = MinStack()
    a.push(-2)
    a.push(0)
    a.push(-3)
    a.min()
    a.pop()
    a.top()
    a.min()