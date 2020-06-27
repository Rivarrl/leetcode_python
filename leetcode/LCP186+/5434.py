# -*- coding: utf-8 -*-
# ======================================
# @File    : 5434.py
# @Time    : 2020/6/27 22:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5434. 删掉一个元素以后全为 1 的最长子数组]()
    """
    @timeit
    def longestSubarray(self, nums: List[int]) -> int:
        last = cur = 0
        nums.append(0)
        n = len(nums)
        res = 0
        cnt = 0
        for i in range(n):
            if nums[i] == 0:
                res = max(res, last + cur)
                last, cur = cur, 0
                cnt += 1
            else:
                cur += 1
        return res - (cnt == 1)

if __name__ == '__main__':
    a = Solution()
    a.longestSubarray(nums = [1,1,0,1])
    a.longestSubarray(nums = [0,1,1,1,0,1,1,0,1])
    a.longestSubarray(nums = [1,1,1])
    a.longestSubarray(nums = [1,1,0,0,1,1,1,0,1])
    a.longestSubarray(nums = [0,0,0])