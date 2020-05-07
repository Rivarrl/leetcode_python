# -*- coding: utf-8 -*-
# ======================================
# @File    : 155.py
# @Time    : 2020/5/7 12:59
# @Author  : Rivarrl
# ======================================
class Node:
    def __init__(self, val, mi, next=None):
        self.val = val
        self.mi = mi
        self.next = next

class MinStack:
    """
    [155. 最小栈](https://leetcode-cn.com/problems/min-stack/)
    """
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        if not self.head:
            self.head = Node(x, x)
        else:
            self.head = Node(x, [x, self.head.mi][x > self.head.mi], self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.mi

if __name__ == '__main__':
    a = MinStack()
    a.push(-2)
    a.push(0)
    a.push(-3)
    a.getMin()
    a.pop()
    a.top()
    a.getMin()