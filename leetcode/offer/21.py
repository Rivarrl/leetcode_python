# -*- coding: utf-8 -*-
# ======================================
# @File    : 21.py
# @Time    : 2020/4/28 15:29
# @Author  : Rivarrl
# ======================================
# [面试题21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)
from algorithm_utils import *
class Solution:
    @timeit
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            while lo < hi and (nums[lo] & 1):
                lo += 1
            while lo < hi and (not nums[hi] & 1):
                hi -= 1
            if lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
        return nums

if __name__ == '__main__':
    a = Solution()
    a.exchange([1,2,3,4])