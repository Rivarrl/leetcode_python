# -*- coding: utf-8 -*-
# ======================================
# @File    : 352.py
# @Time    : 2020/5/8 17:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

import bisect
class SummaryRanges:
    """
    [352. 将数据流变为多个不相交区间](https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals/)
    """
    def __init__(self):
        self.arr = []

    def addNum(self, val: int) -> None:
        i = bisect.bisect(self.arr, val)
        if i & 1: return
        if i < len(self.arr) and self.arr[i] - val == 1:
            self.arr[i] = val
        else:
            self.arr.insert(i, val)
            self.arr.insert(i, val)
        if i > 0 and self.arr[i] - self.arr[i-1] <= 1:
            self.arr.pop(i)
            self.arr.pop(i-1)

    def getIntervals(self) -> List[List[int]]:
        return [[x, y] for x, y in zip(self.arr[::2], self.arr[1::2])]

if __name__ == '__main__':
    a = SummaryRanges()
    a.addNum(1)
    x = a.getIntervals()
    print(x)
    a.addNum(3)
    x = a.getIntervals()
    print(x)
    a.addNum(7)
    x = a.getIntervals()
    print(x)
    a.addNum(2)
    x = a.getIntervals()
    print(x)
    a.addNum(6)
    x = a.getIntervals()
    print(x)