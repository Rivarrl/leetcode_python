# -*- coding: utf-8 -*-
# ======================================
# @File    : 34.py
# @Time    : 2020/5/9 16:57
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
    """
    @timeit
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 一次二分，找到target再分别向左/右逐个移动，O(logn)，遇到大片相等的数组会退化为O(n)
        lo, hi = 0, len(nums)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] > target:
                hi = mi
            elif nums[mi] < target:
                lo = mi + 1
            else:
                l = r = mi
                while l >= 0 and nums[l] == nums[mi]: l -= 1
                while r < len(nums) and nums[r] == nums[mi]: r += 1
                return [l+1, r-1]
        return [-1, -1]

    @timeit
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        # 两次二分，分别找lower_bound和upper_bound
        n = len(nums)
        lo, hi = 0, n
        res = [-1, -1]
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi
        if lo == n or nums[lo] != target: return res
        res[0] = lo
        hi = n - 1
        while lo < hi:
            mi = (lo + hi + 1) >> 1
            if nums[mi] > target:
                hi = mi - 1
            else:
                lo = mi
        res[1] = hi
        return res

if __name__ == '__main__':
    a = Solution()
    a.searchRange2(nums = [5,7,7,8,8,10], target = 8)
    a.searchRange2(nums = [5,7,7,8,8,10], target = 6)
    a.searchRange2(nums = [5,7,8,8,8,10], target = 8)
