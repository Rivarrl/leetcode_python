# -*- coding: utf-8 -*-
# ======================================
# @File    : 45.py
# @Time    : 2020/5/2 14:44
# @Author  : Rivarrl
# ======================================
# [面试题45. 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def minNumber(self, nums: List[int]) -> str:
        nums = [str(e) for e in nums]
        def quick_sort(lo, hi):
            if lo >= hi: return
            i, j = lo, hi
            base = nums[lo]
            while i < j:
                while i < j and nums[j] + base >= base + nums[j]:
                    j -= 1
                while i < j and nums[i] + base <= base + nums[i]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[lo], nums[i] = nums[i], nums[lo]
            quick_sort(lo, i-1)
            quick_sort(i+1, hi)
        quick_sort(0, len(nums)-1)
        return "".join(nums)


if __name__ == '__main__':
    a = Solution()
    a.minNumber([10,2])
    a.minNumber([3,30,34,5,9])
    a.minNumber([9,34,55,8,12,402])