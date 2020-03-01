# -*- coding: utf-8 -*-
# ======================================
# @File    : 211.py
# @Time    : 2019/11/12 9:24
# @Author  : Rivarrl
# ======================================
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.t = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q) > 1:
            self.t.append(self.q.pop(0))
        ret = self.q.pop(0)
        self.t, self.q = self.q, self.t
        return ret

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.q) > 1:
            self.t.append(self.q.pop(0))
        ret = self.q.pop(0)
        self.t.append(ret)
        self.t, self.q = self.q, self.t
        return ret

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()