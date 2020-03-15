# -*- coding: utf-8 -*-
# ======================================
# @File    : 5357.py
# @Time    : 2020/3/15 10:38
# @Author  : Rivarrl
# ======================================
class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = []
        self.ms = maxSize

    def push(self, x: int) -> None:
        if len(self.stk) < self.ms:
            self.stk.append(x)

    def pop(self) -> int:
        if len(self.stk) > 0:
            return self.stk.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stk))):
            self.stk[i] += val

if __name__ == '__main__':
    a = CustomStack(3)
    a.push(1)
    a.push(2)
    a.pop()
    a.push(2)
    a.push(3)
    a.push(4)
    a.increment(5, 100)
    a.increment(2, 100)
    a.pop()
    a.pop()
    a.pop()
    a.pop()