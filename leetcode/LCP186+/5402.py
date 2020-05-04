# -*- coding: utf-8 -*-
# ======================================
# @File    : 5402.py
# @Time    : 2020/5/3 10:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5402. 绝对差不超过限制的最长连续子数组]()
    """
    @timeit
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        def judge(x):
            if x == 1: return True
            stk, stkr = [], []
            for i in range(n):
                if stk and stk[0] < i-x+1:
                    stk = stk[1:]
                if stkr and stkr[0] < i-x+1:
                    stkr = stkr[1:]
                while stk and nums[stk[-1]] <= nums[i]:
                    stk.pop()
                while stkr and nums[stkr[-1]] >= nums[i]:
                    stkr.pop()
                stk.append(i)
                stkr.append(i)
                if i >= x - 1:
                    if nums[stk[0]] - nums[stkr[0]] <= limit: return True
            return False
        lo, hi = 0, n + 1
        while lo + 1 < hi:
            mi = (lo + hi) >> 1
            if judge(mi):
                lo = mi
            else:
                hi = mi
        return lo

if __name__ == '__main__':
    a = Solution()
    a.longestSubarray(nums = [8,2,4,7], limit = 4)
    a.longestSubarray(nums = [10,1,2,4,7,2], limit = 5)
    a.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0)