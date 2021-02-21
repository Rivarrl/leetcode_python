# -*- coding: utf-8 -*-
# ======================================
# @File    : 1438.py
# @Time    : 2021/2/21 18:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1438. 绝对差不超过限制的最长连续子数组](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)
    """
    @timeit
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        n = len(nums)
        qma, qmi = deque(), deque()
        l = r = res = 0
        while r < n:
            while qma and qma[-1] < nums[r]:
                qma.pop()
            while qmi and qmi[-1] > nums[r]:
                qmi.pop()
            qma.append(nums[r])
            qmi.append(nums[r])
            while qma and qmi and qma[0] - qmi[0] > limit:
                if nums[l] == qma[0]:
                    qma.popleft()
                if nums[l] == qmi[0]:
                    qmi.popleft()
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.longestSubarray(nums = [8,2,4,7], limit = 4)
    a.longestSubarray(nums = [10,1,2,4,7,2], limit = 5)
    a.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0)