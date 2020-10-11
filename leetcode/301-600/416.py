# -*- coding: utf-8 -*-
# ======================================
# @File    : 416.py
# @Time    : 2020/10/11 17:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [416. 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)
    """
    @timeit
    def canPartition(self, nums: List[int]) -> bool:
        # 背包问题，有无能和为sum(nums)//2的集合
        s = sum(nums)
        if s & 1: return False
        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True
        nums.sort()
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                if dp[j - nums[i]]:
                    dp[j] = True
            if dp[-1]: return True
        return False


if __name__ == '__main__':
    a = Solution()
    a.canPartition([1, 5, 11, 5])
    a.canPartition([1, 2, 3, 5])
    a.canPartition([1,2,5])