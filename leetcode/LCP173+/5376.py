# -*- coding: utf-8 -*-
# ======================================
# @File    : 5376.py
# @Time    : 2020/4/5 10:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5376. 非递增顺序的最小子序列]()
    """
    @timeit
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s = sum(nums)
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre > s - pre:
                return nums[:i+1]




if __name__ == '__main__':
    a = Solution()
    a.minSubsequence([4,3,10,9,8])
    a.minSubsequence([4,4,7,6,7])
    a.minSubsequence([6])
    a.minSubsequence([1,1])