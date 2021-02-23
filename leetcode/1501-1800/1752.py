# -*- coding: utf-8 -*-
# ======================================
# @File    : 1752
# @Time    : 2021/2/20 13:45
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1752. 检查数组是否经排序和轮转得到](https://leetcode-cn.com/problems/check-if-array-is-sorted-and-rotated/)
    """
    @timeit
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        i = nums.index(min(nums))
        if i == 0 and nums[i] == nums[-1]:
            j = n - 1
            while j > i and nums[j] == nums[i]:
                j -= 1
            i = (j + 1) % n
        k = (i + n - 1) % n
        while i != k:
            j = (i+1) % n
            if nums[i] > nums[j]: return False
            i = j
        return True

if __name__ == '__main__':
    a = Solution()
    a.check(nums = [3,4,5,1,2])
    a.check(nums = [2,1,3,4])
    a.check(nums = [1,2,3])
    a.check(nums = [1,1,1])
    a.check(nums = [6,10,6])