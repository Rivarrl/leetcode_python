# -*- coding: utf-8 -*-
# ======================================
# @File    : 1749.py
# @Time    : 2021/2/17 19:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1749. 任意子数组和的绝对值的最大值](https://leetcode-cn.com/problems/maximum-absolute-sum-of-any-subarray/)
    """
    @timeit
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = -1
        y = z = 0
        for x in nums:
            if y < 0:
                y = 0
            if  z > 0:
                z = 0
            y += x
            z += x
            res = max(res, y, abs(z))
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxAbsoluteSum(nums = [1,-3,2,3,-4])
    a.maxAbsoluteSum(nums = [2,-5,1,-4,3,-2])