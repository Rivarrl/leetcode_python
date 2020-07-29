# -*- coding: utf-8 -*-
# ======================================
# @File    : 03-04.py
# @Time    : 2020/7/30 0:29
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        for i in range(len(self.stk1)):
            self.stk2.append(self.stk1.pop())
        x = self.stk2.pop()
        for i in range(len(self.stk2)):
            self.stk1.append(self.stk2.pop())
        return x

    def peek(self) -> int:
        for i in range(len(self.stk1)):
            self.stk2.append(self.stk1.pop())
        x = self.stk2[-1]
        for i in range(len(self.stk2)):
            self.stk1.append(self.stk2.pop())
        return x

    def empty(self) -> bool:
        return self.stk1 == []


if __name__ == '__main__':
    a = MyQueue()
    a.push(1)
    a.pop()
    a.peek()
    a.empty()