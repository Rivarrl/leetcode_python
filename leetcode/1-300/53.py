# -*- coding: utf-8 -*-
# ======================================
# @File    : 53.py
# @Time    : 2020/5/3 0:11
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)

if __name__ == '__main__':
    a = Solution()
    a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])