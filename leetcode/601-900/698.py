# -*- coding: utf-8 -*-
# ======================================
# @File    : 698.py
# @Time    : 2021/3/3 23:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [698. 划分为k个相等的子集](https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/)
    """
    @timeit
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()

if __name__ == '__main__':
    a = Solution()
    a.canPartitionKSubsets(nums = [4, 3, 2, 3, 5, 2, 1], k = 4)