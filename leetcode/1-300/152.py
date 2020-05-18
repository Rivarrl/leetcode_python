# -*- coding: utf-8 -*-
# ======================================
# @File    : 152.py
# @Time    : 2020/5/18 22:11
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)
    """
    @timeit
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        res = dp[0][0] = dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1] * nums[i], nums[i])
            dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1] * nums[i], nums[i])
            res = max(res, dp[i][0])
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxProduct([2,3,-2,4])
    a.maxProduct([-2,0,-1])