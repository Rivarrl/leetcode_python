# -*- coding: utf-8 -*-
# ======================================
# @File    : 462.py
# @Time    : 2020/12/1 1:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [462. 最少移动次数使数组元素相等 II](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/)
    """
    @timeit
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n & 1:
            return sum(abs(e-nums[n//2]) for e in nums)
        else:
            return min(sum(abs(e-nums[n//2]) for e in nums), sum(abs(e-nums[n//2-1]) for e in nums))

if __name__ == '__main__':
    a = Solution()
    a.minMoves2([1,2,3])
    a.minMoves2([1,2,3,6])