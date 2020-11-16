# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-20.py
# @Time    : 2020/11/16 12:48 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import heapq

class MedianFinder:
    """
    [面试题 17.20. 连续中值](https://leetcode-cn.com/problems/continuous-median-lcci/)
    """
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.n = 0

    def addNum(self, num: int) -> None:
        if self.n & 1:
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        self.n += 1

    @timeit
    def findMedian(self) -> float:
        if self.n & 1:
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2

if __name__ == '__main__':
    a = MedianFinder()
    a.addNum(1)
    a.addNum(2)
    a.findMedian()
    a.addNum(3)
    print(a.min_heap, a.max_heap)
    a.findMedian()
