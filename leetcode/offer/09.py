# -*- coding: utf-8 -*-
# ======================================
# @File    : 09.py
# @Time    : 2020/4/21 13:41
# @Author  : Rivarrl
# ======================================
# [面试题09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)
from algorithm_utils import *

class CQueue:
    # 一个添加用，一个弹出用，不弹出就不倒腾两个stk的内容
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def appendTail(self, value: int) -> None:
        self.stk1.append(value)

    def deleteHead(self) -> int:
        if not self.stk2:
            if not self.stk1:
                return -1
            while self.stk1:
                self.stk2.append(self.stk1.pop())
        return self.stk2.pop()


if __name__ == '__main__':
    cq = CQueue()
    cq.appendTail(3)
    cq.deleteHead()
    cq.deleteHead()