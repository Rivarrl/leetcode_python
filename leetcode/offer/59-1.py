# -*- coding: utf-8 -*-
# ======================================
# @File    : 59-1.py
# @Time    : 2020/5/1 19:16
# @Author  : Rivarrl
# ======================================
# [面试题59 - I.滑动窗口的最大值](https: // leetcode - cn.com / problems / hua - dong - chuang - kou - de - zui - da - zhi - lcof /)
from algorithm_utils import *

class Solution:
    @timeit
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stk, res = [], []
        for i in range(n):
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
            stk.append(i)
            while stk and stk[0] + k <= i:
                stk.pop(0)
            if i >= k - 1:
                res.append(nums[stk[0]])
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    a.maxSlidingWindow([1,-1], 1)