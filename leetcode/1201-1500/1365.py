# -*- coding: utf-8 -*-
# ======================================
# @File    : 1365.py
# @Time    : 2020/10/26 12:44 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1365. 有多少小于当前数字的数字](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
    """
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        arr = nums[:]
        arr.sort()
        for i in range(len(nums)):
            if arr[i] not in d:
                d[arr[i]] = i
        res = [d[e] for e in nums]
        return res

if __name__ == '__main__':
    a = Solution()
    a.smallerNumbersThanCurrent(nums = [8,1,2,2,3])
    a.smallerNumbersThanCurrent(nums = [6,5,4,8])
    a.smallerNumbersThanCurrent(nums = [7,7,7,7])