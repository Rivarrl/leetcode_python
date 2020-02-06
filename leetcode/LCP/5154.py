# -*- coding: utf-8 -*-
# ======================================
# @File    : 5154.py
# @Time    : 1/25/20 11:00 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5154. 翻转子数组得到最大的数组值](https://leetcode-cn.com/problems/reverse-subarray-to-maximize-array-value/)
    """
    @timeit
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        ceiling, floor = min(nums[:2]), max(nums[:2])
        inc = 0
        for x, y in zip(nums, nums[1:]):
            inc = max(inc, abs(y - nums[0]) - abs(y - x))
        for x, y in zip(nums, nums[1:]):
            inc = max(inc, abs(x - nums[-1]) - abs(y - x))
        for x, y in zip(nums, nums[1:]):
            lo, hi = sorted([x, y])
            inc = max(inc, 2 * (ceiling - hi), 2 * (lo - floor))
            if lo > ceiling: ceiling = lo
            if hi < floor: floor = hi
        ans = 0
        for x, y in zip(nums, nums[1:]):
            ans += abs(x - y)
        return ans + inc


if __name__ == '__main__':
    a = Solution()
    a.maxValueAfterReverse([2,3,1,5,4])
    a.maxValueAfterReverse([2,4,9,24,2,1,10])