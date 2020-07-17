# -*- coding: utf-8 -*-
# ======================================
# @File    : 35.py
# @Time    : 2020/7/17 12:58 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)
    """
    @timeit
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] >= target:
                hi = mi
            else:
                lo = mi + 1
        return lo

if __name__ == '__main__':
    a = Solution()
    a.searchInsert([1,3,5,6],5)
    a.searchInsert([1,3,5,6],2)
    a.searchInsert([1,3,5,6],7)
    a.searchInsert([1,3,5,6],0)
