# -*- coding: utf-8 -*-
# ======================================
# @File    : 300.py
# @Time    : 2020/3/14 11:07
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [300. 最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
    """
    @timeit
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    @timeit
    def lengthOfLIS2(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = []
        for i in range(n):
            if not dp or dp[-1] < nums[i]:
                dp.append(nums[i])
            else:
                lo, hi = 0, len(dp) - 1
                while lo < hi:
                    mid = lo + hi >> 1
                    if dp[mid] >= nums[i]:
                        hi = mid
                    else:
                        lo = mid + 1
                dp[lo] = nums[i]
        return len(dp)


if __name__ == '__main__':
    a = Solution()
    a.lengthOfLIS2([1,3,6,7,9,4,10,5,6])
    # a.lengthOfLIS2([10,9,2,5,3,7,101,18])
    # a.lengthOfLIS2([2,2])