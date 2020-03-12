# -*- coding: utf-8 -*-
# ======================================
# @File    : 53-2.py
# @Time    : 2020/3/13 0:23
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# [面试题53 - II. 0～n-1中缺失的数字](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/)
class Solution:
    @timeit
    def missingNumber(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + hi >> 1
            if nums[mid] != mid:
                hi = mid
            else:
                lo = mid + 1
        return lo

if __name__ == '__main__':
    a = Solution()
    a.missingNumber([0,1,3])
    a.missingNumber([0,1,2,3,4,5,6,7,9])
    a.missingNumber([0])