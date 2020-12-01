# -*- coding: utf-8 -*-
# ======================================
# @File    : 1670.py
# @Time    : 2020/12/2 0:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class FrontMiddleBackQueue:
    """
    [1670. 设计前中后队列]()
    """
    def __init__(self):
        self.stk = []

    def pushFront(self, val: int) -> None:
        self.stk = [val] + self.stk

    def pushMiddle(self, val: int) -> None:
        mi = len(self.stk) >> 1
        self.stk = self.stk[:mi] + [val] + self.stk[mi:]

    def pushBack(self, val: int) -> None:
        self.stk.append(val)

    @timeit
    def popFront(self) -> int:
        return -1 if not self.stk else self.stk.pop(0)

    @timeit
    def popMiddle(self) -> int:
        return -1 if not self.stk else self.stk.pop(len(self.stk) - 1 >> 1)

    @timeit
    def popBack(self) -> int:
        return -1 if not self.stk else self.stk.pop()


if __name__ == '__main__':
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    print(q.stk)
    q.pushBack(2)
    print(q.stk)
    q.pushMiddle(3)
    print(q.stk)
    q.pushMiddle(4)
    print(q.stk)
    q.popFront()
    q.popMiddle()
    q.popMiddle()
    q.popBack()
    q.popFront()