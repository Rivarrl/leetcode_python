# -*- coding: utf-8 -*-
# ======================================
# @File    : 53-1.py
# @Time    : 2020/4/28 23:40
# @Author  : Rivarrl
# ======================================
# [面试题53 - I. 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] < target:
                lo = mi + 1
            elif nums[mi] > target:
                hi = mi - 1
            else:
                lo = hi = mi
                break
        else:
            return 0
        while lo >= 0 and nums[lo] == target:
            lo -= 1
        while hi < n and nums[hi] == target:
            hi += 1
        return hi - lo - 1

if __name__ == '__main__':
    a = Solution()
    a.search([5,7,7,8,8,10], 8)
    a.search([5,7,7,8,8,10], 6)