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
    思路：数据流是动态的，所以add里面sort是不合理的做法
    要求是只需要找到第K大元素，其它元素的顺序可以无序
    维护一个最小堆，大小为K，堆顶的元素就是第K大的元素
    """
    def __init__(self, k: int, nums: List[int]):
        self.arr = [-float('inf')] * k
        self.k = k
        for x in nums: self.add(x)

    def sink(self, i):
        j, l, r = i, i * 2 + 1, i * 2 + 2
        if l < self.k and self.arr[l] < self.arr[j]:
            j = l
        if r < self.k and self.arr[r] < self.arr[j]:
            j = r
        if j != i:
            self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
            self.sink(j)

    def add(self, val: int) -> int:
        if val > self.arr[0]:
            self.arr[0] = val
            self.sink(0)
        return self.arr[0]


if __name__ == '__main__':
    # Your KthLargest object will be instantiated and called as such:
    k = 4
    nums = [4,5,8,2]
    obj = KthLargest(k, nums)
    param_1 = obj.add(3)
    print(param_1)