# -*- coding: utf-8 -*-
# ======================================
# @File    : 5180.py
# @Time    : 2020/4/26 16:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5180. 带限制的子序列和](https://leetcode-cn.com/problems/constrained-subset-sum)
    """
    @timeit
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        stk = [(nums[0], 0)]
        for i in range(1, n):
            cur_max = stk[0][0]
            if cur_max >= 0:
                dp[i] = cur_max + nums[i]
            else:
                dp[i] = nums[i]
            while stk and stk[-1][0] <= dp[i]:
                stk.pop()
            stk.append((dp[i], i))
            while stk[0][1] < i - k + 1:
                stk.pop(0)
        return max(dp)

if __name__ == '__main__':
    a = Solution()
    a.constrainedSubsetSum(nums = [10,2,-10,5,20], k = 2)
    a.constrainedSubsetSum(nums = [-1,-2,-3], k = 1)
    a.constrainedSubsetSum(nums = [10,-2,-10,-5,20], k = 2)