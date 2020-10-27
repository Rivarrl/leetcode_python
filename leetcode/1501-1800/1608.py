# -*- coding: utf-8 -*-
# ======================================
# @File    : 1608.py
# @Time    : 2020/10/27 12:49 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1608. 特殊数组的特征值](https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x/)
    """
    @timeit
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = j = 0
        while i <= n and j < n:
            while i <= n and i <= nums[j]:
                if i == n - j: return i
                i += 1
            while j < n and i > nums[j]:
                j += 1
        return -1

if __name__ == '__main__':
    a = Solution()
    a.specialArray(nums = [3,5])
    a.specialArray(nums = [0,0])
    a.specialArray(nums = [0,4,3,0,4])
    a.specialArray(nums = [3,6,7,7,0])