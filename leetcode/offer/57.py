# -*- coding: utf-8 -*-
# ======================================
# @File    : 57.py
# @Time    : 2020/3/12 23:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lo, hi = 0, n-1
        while lo < hi:
            if nums[lo] + nums[hi] == target:
                return [nums[lo], nums[hi]]
            if nums[lo] + nums[hi] < target:
                lo += 1
            else:
                hi -= 1
        return []

if __name__ == '__main__':
    a = Solution()
    a.twoSum(nums=[2,7,11,15], target = 9)