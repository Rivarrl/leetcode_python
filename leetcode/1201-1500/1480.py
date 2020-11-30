# -*- coding: utf-8 -*-
# ======================================
# @File    : 1480.py
# @Time    : 2020/12/1 0:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1480. 一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array/)
    """
    @timeit
    def runningSum(self, nums: List[int]) -> List[int]:
        pre = []
        c = 0
        for x in nums:
            c += x
            pre.append(c)
        return pre

if __name__ == '__main__':
    a = Solution()
    a.runningSum(nums = [1,2,3,4])
    a.runningSum(nums = [1,1,1,1,1])
    a.runningSum(nums = [3,1,2,10,1])