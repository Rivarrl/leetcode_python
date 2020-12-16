# -*- coding: utf-8 -*-
# ======================================
# @File    : 622.py
# @Time    : 2020/12/16 3:17 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class MyCircularQueue:
    """
    [622. 设计循环队列](https://leetcode-cn.com/problems/design-circular-queue/)
    """
    def __init__(self, k: int):
        self.k = k
        self.q = [-1] * k
        self.size, self.left, self.right = 0, 0, 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.k: return False
        self.q[self.right] = value
        self.right = (self.right + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0: return False
        self.q[self.left] = -1
        self.left = (self.left + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0: return -1
        return self.q[self.left]

    def Rear(self) -> int:
        if self.size == 0: return -1
        return self.q[(self.right - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

if __name__ == '__main__':
    q = MyCircularQueue(3)
    print(q.enQueue(1)) # T
    print(q.enQueue(2)) # T
    print(q.enQueue(3)) # T
    print(q.enQueue(4)) # F
    print(q.Rear()) # 3
    print(q.isFull()) # T
    print(q.deQueue()) # T
    print(q.q)
    print(q.Front())
    print(q.enQueue(4)) # T
    print(q.Rear()) # 4