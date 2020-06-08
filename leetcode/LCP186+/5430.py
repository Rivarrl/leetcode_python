# -*- coding: utf-8 -*-
# ======================================
# @File    : 5430.py
# @Time    : 2020/6/7 11:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Node:
    def __init__(self, val, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next

class BrowserHistory:
    """
    [5430. 设计浏览器历史记录](https://leetcode-cn.com/problems/design-browser-history/)
    """
    def __init__(self, homepage: str):
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        p = Node(url)
        self.cur.next = p
        p.pre = self.cur
        self.cur = p

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.cur.pre:
            self.cur = self.cur.pre
            i += 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.cur.next:
            self.cur = self.cur.next
            i += 1
        return self.cur.val

if __name__ == '__main__':
    a = BrowserHistory("leetcode.com")
    a.visit("google.com")
    a.visit("facebook.com")
    a.visit("youtube.com")
    a.back(1)
    a.back(1)
    a.forward(1)
    a.visit("linkedin.com")
    a.forward(2)
    a.back(2)
    a.back(7)