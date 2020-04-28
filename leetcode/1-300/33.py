# -*- coding: utf-8 -*-
# ======================================
# @File    : 33.py
# @Time    : 2020/4/27 12:51
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)
    """
    @timeit
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] == target:
                return mi
            if nums[mi] >= nums[lo]:
                if nums[mi] > target >= nums[lo]:
                    hi = mi - 1
                else:
                    lo = mi + 1
            else:
                if nums[mi] < target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
        return -1


if __name__ == '__main__':
    a = Solution()
    a.search([4,5,6,7,0,1,2], 0)
    a.search([4,5,6,7,0,1,2], 3)
    a.search([3,1],1)
    a.search([1,2,3],1)