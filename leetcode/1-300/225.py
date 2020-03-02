# -*- coding: utf-8 -*-
# ======================================
# @File    : 211.py
# @Time    : 2019/11/12 9:24
# @Author  : Rivarrl
# ======================================
class MyStack:
    """
    [225. 用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues/)
    """
    def __init__(self):
        self.q = []
        self.t = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        while len(self.q) > 1:
            self.t.append(self.q.pop(0))
        ret = self.q.pop(0)
        self.t, self.q = self.q, self.t
        return ret

    def top(self) -> int:
        while len(self.q) > 1:
            self.t.append(self.q.pop(0))
        ret = self.q.pop(0)
        self.t.append(ret)
        self.t, self.q = self.q, self.t
        return ret

    def empty(self) -> bool:
        return len(self.q) == 0
