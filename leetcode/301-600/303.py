# -*- coding: utf-8 -*-
# ======================================
# @File    : 303.py
# @Time    : 2019/11/10 23:57
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class NumArray:
    """
    [303. 区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable/)
    思路：前缀和基本操作
    """
    def __init__(self, nums: List[int]):
        self.pre = [0]
        for e in nums:
            self.pre += [self.pre[-1] + e]

    @timeit
    def sumRange(self, i: int, j: int) -> int:
        return self.pre[j+1] - self.pre[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
if __name__ == '__main__':
    na = NumArray([-2, 0, 3, -5, 2, -1])
    na.sumRange(0, 2)
    na.sumRange(2, 5)
    na.sumRange(0, 5)
    na.sumRange(5, 5)