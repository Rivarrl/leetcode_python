# -*- coding: utf-8 -*-
# ======================================
# @File    : 540.py
# @Time    : 2020/5/9 1:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [540. 有序数组中的单一元素](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/)
    """
    @timeit
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        while lo + 1 < hi:
            mi = lo + (hi - lo) // 2
            if mi & 1 == 0: mi += 1
            if nums[mi] == nums[mi-1]:
                lo = mi + 1
            else:
                hi = mi
        return nums[lo]

if __name__ == '__main__':
    a = Solution()
    a.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
    a.singleNonDuplicate([3,3,7,7,10,11,11])
    a.singleNonDuplicate([1,1,2,2,3])