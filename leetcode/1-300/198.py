# -*- coding: utf-8 -*-
# ======================================
# @File    : 198.py
# @Time    : 2020/5/29 0:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)
    """
    @timeit
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        if n == 3: return max(nums[0]+nums[2], nums[1])
        dp = [0] * n
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
        res = max(dp[:3])
        for i in range(3, n):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
            res = max(res, dp[i])
        return res

if __name__ == '__main__':
    a = Solution()
    a.rob([1,2,3,1])
    a.rob([2,7,9,3,1])