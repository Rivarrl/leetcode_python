# -*- coding: utf-8 -*-
# ======================================
# @File    : 209.py
# @Time    : 2020/6/28 11:53 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [209. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum)
    """
    @timeit
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        from collections import deque
        q = deque()
        res, cur = 0x3f3f3f3f, 0
        n = len(nums)
        for i in range(n):
            cur += nums[i]
            q.append(i)
            while q and cur >= s:
                j = q.popleft()
                cur -= nums[j]
                res = min(res, i + 1 - j)
        return res if res != 0x3f3f3f3f else 0

if __name__ == '__main__':
    a = Solution()
    a.minSubArrayLen(s = 7, nums = [2,3,1,2,4,3])
    a.minSubArrayLen(4, [1,4,4])