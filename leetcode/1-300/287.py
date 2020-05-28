# -*- coding: utf-8 -*-
# ======================================
# @File    : 287.py
# @Time    : 2020/5/26 12:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)
    """
    @timeit
    def findDuplicate(self, nums: List[int]) -> int:
        # 二分答案
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mi = lo + (hi - lo) // 2
            cnt = 0
            for i in range(n):
                if nums[i] <= mi:
                    cnt += 1
            if cnt > mi:
                hi = mi
            else:
                lo = mi + 1
        return hi

    @timeit
    def findDuplicate2(self, nums: List[int]) -> int:
        # floyd判圈
        p = slow = fast = 0
        while p == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            p = 1
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

if __name__ == '__main__':
    a = Solution()
    a.findDuplicate([1,3,4,2,2])
    a.findDuplicate([3,1,3,4,2])