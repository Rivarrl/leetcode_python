# -*- coding: utf-8 -*-
# ======================================
# @File    : 713.py
# @Time    : 2020/12/23 2:05 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [713. 乘积小于K的子数组](https://leetcode-cn.com/problems/subarray-product-less-than-k/)
    """
    @timeit
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right, cur, res = 0, 0, 1, 0
        while left <= right < n:
            cur *= nums[right]
            while left <= right and cur >= k:
                cur //= nums[left]
                left += 1
            res += (right + 1 - left)
            right += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100)
    a.numSubarrayProductLessThanK([1,2,3], 0)