# -*- coding: utf-8 -*-
# ======================================
# @File    : 307.py
# @Time    : 2019/12/4 10:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Segment:
    def __init__(self, l=None, r=None, res=None):
        self.l = l
        self.r = r
        self.res = res

class NumArray:
    """
    [307. 区域和检索 - 数组可修改](https://leetcode-cn.com/problems/range-sum-query-mutable/)
    思路：线段树模板题
    """
    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.nums = nums
        self.st = [Segment() for _ in range(4*self.N+5)]
        self.build(1, 1, self.N)

    def build(self, p, l, r):
        self.st[p].l, self.st[p].r = l, r
        if l == r:
            self.st[p].res = self.nums[l-1]
            return
        mid = (l + r) // 2
        self.build(p*2,l, mid)
        self.build(p*2+1,mid+1, r)
        self.st[p].res = self.st[p*2].res + self.st[p*2+1].res

    def change(self, p, x, val):
        if self.st[p].l == self.st[p].r:
            self.st[p].res = val
            return
        mid = (self.st[p].l + self.st[p].r) // 2
        if x <= mid: self.change(p*2, x, val)
        else: self.change(p*2+1, x, val)
        self.st[p].res = self.st[p*2].res + self.st[p*2+1].res

    def search(self, p, l, r):
        # p区间是[l,r]的子集
        if self.st[p].l >= l and self.st[p].r <= r:
            return self.st[p].res
        # 无交集
        if self.st[p].r < l or self.st[p].l > r:
            return 0
        # 重叠
        res = 0
        # 左子重叠？
        if self.st[p*2].r >= l:
            res += self.search(p*2, l, r)
        # 右子重叠？
        if self.st[p*2+1].l <= r:
            res += self.search(p*2+1, l, r)
        return res

    def update(self, i: int, val: int) -> None:
        self.change(1, i+1, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.search(1, i+1, j+1)


if __name__ == '__main__':
    # Your NumArray object will be instantiated and called as such:
    obj = NumArray([1,3,5])
    obj.update(1, 2)
    param_2 = obj.sumRange(0,2)
    print(param_2)