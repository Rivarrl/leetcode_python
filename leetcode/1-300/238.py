# -*- coding: utf-8 -*-
# ======================================
# @File    : 238.py
# @Time    : 2020/6/4 0:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for x in nums:
            res.append(res[-1] * x)
        r = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= r
            r *= nums[i]
        return res[:-1]

if __name__ == '__main__':
    a = Solution()
    a.productExceptSelf([1,2,3,4])