# -*- coding: utf-8 -*-
# ======================================
# @File    : 03-01.py
# @Time    : 2020/11/13 1:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class TripleInOne:
    """
    [面试题 03.01. 三合一](https://leetcode-cn.com/problems/three-in-one-lcci/)
    """
    def __init__(self, stackSize: int):
        self.n = stackSize
        self.idx = [0, stackSize, 2 * stackSize]
        self.lr = [[0, stackSize], [stackSize, stackSize*2], [stackSize*2, stackSize*3]]
        self.arr = [0] * (stackSize * 3)

    def push(self, stackNum: int, value: int) -> None:
        if self.idx[stackNum] == self.lr[stackNum][1]: return
        self.arr[self.idx[stackNum]] = value
        self.idx[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if self.idx[stackNum] == self.lr[stackNum][0]: return -1
        self.idx[stackNum] -= 1
        res = self.arr[self.idx[stackNum]]
        return res

    def peek(self, stackNum: int) -> int:
        if self.idx[stackNum] == self.lr[stackNum][0]: return -1
        return self.arr[self.idx[stackNum] - 1]

    def isEmpty(self, stackNum: int) -> bool:
        return self.idx[stackNum] == self.lr[stackNum][0]


if __name__ == '__main__':
    a = TripleInOne(2)
    a.push(0, 1)
    a.push(0, 2)
    a.push(0, 3)
    a.pop(0)
    a.pop(0)
    a.pop(0)
    a.peek(0)