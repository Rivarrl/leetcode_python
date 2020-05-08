# -*- coding: utf-8 -*-
# ======================================
# @File    : 933.py
# @Time    : 2020/5/8 22:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from collections import deque
class RecentCounter:
    """
    [933. 最近的请求次数](https://leetcode-cn.com/problems/number-of-recent-calls/)
    """
    def __init__(self):
        self.stk = deque()

    def ping(self, t: int) -> int:
        while self.stk and self.stk[0] < t - 3000:
            self.stk.popleft()
        self.stk.append(t)
        return len(self.stk)

if __name__ == '__main__':
    a = RecentCounter()
    a.ping(1)
    a.ping(100)
    a.ping(3001)
    a.ping(3002)
