# -*- coding: utf-8 -*-
# ======================================
# @File    : 5630.py
# @Time    : 2020/12/20 12:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5630. 删除子数组的最大得分](https://leetcode-cn.com/problems/maximum-erasure-value/)
    """
    @timeit
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ss = {}
        j = 0
        res = w = 0
        for i in range(n):
            if nums[i] in ss:
                tmp, j = j, ss[nums[i]] + 1
                for k in range(tmp, ss[nums[i]]+1):
                    del ss[nums[k]]
                    w -= nums[k]
            ss[nums[i]] = i
            w += nums[i]
            res = max(res, w)
        return res


if __name__ == '__main__':
    a = Solution()
    a.maximumUniqueSubarray(nums = [4,2,4,5,6])
    a.maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5])