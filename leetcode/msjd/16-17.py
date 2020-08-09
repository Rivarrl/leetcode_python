# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-17.py
# @Time    : 2020/8/9 1:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.17. 连续数列](https://leetcode-cn.com/problems/contiguous-sequence-lcci/)
    """
    @timeit
    def maxSubArray(self, nums: List[int]) -> int:
        res = m = -(1<<64)
        for x in nums:
            m = max(m+x, x)
            res = max(res, m)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])