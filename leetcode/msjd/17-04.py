# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-04.py
# @Time    : 2020/6/30 22:07
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.04. 消失的数字](https://leetcode-cn.com/problems/missing-number-lcci/)
    """
    @timeit
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, x in enumerate(nums):
            res ^= i
            res ^= x
        return res

if __name__ == '__main__':
    a = Solution()
    a.missingNumber([3,0,1])
    a.missingNumber([9,6,4,2,3,5,7,0,1])