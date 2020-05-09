# -*- coding: utf-8 -*-
# ======================================
# @File    : 528.py
# @Time    : 2020/5/9 13:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import bisect, random
class Solution:
    """
    [528. 按权重随机选择](https://leetcode-cn.com/problems/random-pick-with-weight/)
    """
    def __init__(self, w: List[int]):
        self.arr = [0]
        for x in w: self.arr += [self.arr[-1] + x]
        self.arr = self.arr[1:]

    def pickIndex(self) -> int:
        rd = random.randint(1, self.arr[-1])
        idx = bisect.bisect_left(self.arr, rd)
        return idx

if __name__ == '__main__':
    a = Solution([1])
    a.pickIndex()
    a = Solution([1,3])
    a.pickIndex()
    a.pickIndex()
    a.pickIndex()
    a.pickIndex()
    a.pickIndex()