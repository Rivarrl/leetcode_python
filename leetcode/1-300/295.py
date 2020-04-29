# -*- coding: utf-8 -*-
# ======================================
# @File    : 295.py
# @Time    : 2020/4/29 22:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import heapq

class MedianFinder:
    """
    [295. 数据流的中位数](https://leetcode-cn.com/problems/find-median-from-data-stream/)
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ctr = 0
        self.q = []
        self.q2 = []

    def addNum(self, num: int) -> None:
        if self.ctr == 0:
            heapq.heappush(self.q, -num)
        else:
            if num > -self.q[0]:
                heapq.heappush(self.q2, num)
            else:
                heapq.heappush(self.q, -num)
            if self.ctr & 1 and len(self.q) > len(self.q2):
                x = -heapq.heappop(self.q)
                heapq.heappush(self.q2, x)
            elif len(self.q) < len(self.q2):
                x = heapq.heappop(self.q2)
                heapq.heappush(self.q, -x)
        self.ctr += 1

    @timeit
    def findMedian(self) -> float:
        if self.ctr == 0: return 0
        elif self.ctr & 1:
            return -self.q[0]
        else:
            return (self.q2[0] - self.q[0]) / 2

if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    mf.findMedian()
    mf.addNum(3)
    mf.findMedian()