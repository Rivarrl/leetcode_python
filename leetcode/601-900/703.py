# -*- coding: utf-8 -*-
# ======================================
# @File    : 703.py
# @Time    : 2019/11/20 0:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class KthLargest:
    """
    [703. 数据流中的第K大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/)
    """
    def __init__(self, k: int, nums: List[int]):
        self.heap = [-float('inf')] * k
        self.k = k
        self.size = 0
        for i in nums:
            self.add(i)

    def sink(self, i):
        c = (i + 1) * 2 - 1
        while c < len(self.heap):
            if c + 1 < len(self.heap) and self.heap[c + 1] < self.heap[c]:
                c += 1
            if self.heap[i] > self.heap[c]:
                self.heap[i], self.heap[c] = self.heap[c], self.heap[i]
                i = c
                c = (i + 1) * 2 - 1
            else:
                break

    def swim(self, i):
        p = i - 1 // 2
        while p >= 0 and self.heap[p] > self.heap[i]:
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p
            p = (i - 1) // 2

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            if val > self.heap[0]:
                self.heap[0] = val
                self.sink(0)
        else:
            self.heap[self.size] = val
            self.size += 1
            self.swim(self.size - 1)
        return self.heap[0]


if __name__ == '__main__':
    # Your KthLargest object will be instantiated and called as such:
    k = 3
    nums = [4,5,8,2]
    obj = KthLargest(k, nums)
    param_1 = obj.add(5)
    print(param_1)