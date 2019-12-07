# -*- coding: utf-8 -*-
# ======================================
# @File    : 5275.py
# @Time    : 2019/11/9 16:24
# @Author  : Rivarrl
# ======================================

from algorithm_utils import *

class Solution:
    @timeit
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)
        思路：哈希表，将target - nums[i]的索引存到dict中，发现nums[i]在dict中已经存在，就返回[dict[nums[i]], i]
        """
        d = {}
        for i, e in enumerate(nums):
            if e in d:
                return [d[e], i]
            d[target-e] = i

if __name__ == '__main__':
    sol = Solution()
    sol.twoSum([2,7,11,15], 9)
