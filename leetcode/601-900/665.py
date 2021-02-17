# -*- coding: utf-8 -*-
# ======================================
# @File    : 665.py
# @Time    : 2021/2/7 23:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [665. 非递减数列](https://leetcode-cn.com/problems/non-decreasing-array/)
    """
    @timeit
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                cnt += 1
                if cnt > 1: return False
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
        return True

if __name__ == '__main__':
    a = Solution()
    a.checkPossibility(nums = [4,2,3])
    a.checkPossibility(nums = [4,2,1])
    a.checkPossibility([1,4,1,2])
    a.checkPossibility([1,4,4,2])
    a.checkPossibility([1,4,4,2,3])