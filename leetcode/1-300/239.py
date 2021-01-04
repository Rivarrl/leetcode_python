# -*- coding: utf-8 -*-
# ======================================
# @File    : 239.py
# @Time    : 2021/1/2 0:13
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)
    """
    @timeit
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        n = len(nums)
        res = []
        q = deque()
        for i in range(n):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
    a.maxSlidingWindow(nums = [1], k = 1)
    a.maxSlidingWindow(nums = [1,-1], k = 1)
    a.maxSlidingWindow(nums = [9,11], k = 2)
    a.maxSlidingWindow(nums = [4,-2], k = 2)