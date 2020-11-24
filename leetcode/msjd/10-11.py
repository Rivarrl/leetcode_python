# -*- coding: utf-8 -*-
# ======================================
# @File    : 10-11.py
# @Time    : 2020/11/25 0:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        for i in range(0, n-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

if __name__ == '__main__':
    a = Solution()
    a.wiggleSort([5,3,1,2,3])