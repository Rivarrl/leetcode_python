# -*- coding: utf-8 -*-
# ======================================
# @File    : 42.py
# @Time    : 2020/5/4 21:11
# @Author  : Rivarrl
# ======================================
# [面试题42. 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


if __name__ == '__main__':
    a = Solution()
    a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])