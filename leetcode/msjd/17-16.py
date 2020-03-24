# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-16.py
# @Time    : 2020/3/24 0:04
# @Author  : Rivarrl
# ======================================
# [面试题 17.16. 按摩师](https://leetcode-cn.com/problems/the-masseuse-lcci/)

from algorithm_utils import *

class Solution:
    """
    类似于跳跃游戏，每次可选择跳一格和两格
    """
    @timeit
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        return max(dp)

if __name__ == '__main__':
    a = Solution()
    a.massage([1,2,3,1])
    a.massage([2,7,9,3,1])
    a.massage([2,1,4,5,3,1,1,3])