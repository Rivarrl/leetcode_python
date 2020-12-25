# -*- coding: utf-8 -*-
# ======================================
# @File    : 719.py
# @Time    : 2020/12/25 10:08 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [719. 找出第 k 小的距离对](https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/)
    """
    @timeit
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def f(x):
            res = i = 0
            for j in range(1, n):
                while nums[j] - nums[i] > x:
                    i += 1
                res += j - i
            return res
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mi = lo + hi >> 1
            if f(mi) < k:
                lo = mi + 1
            else:
                hi = mi
        return lo

if __name__ == '__main__':
    a = Solution()
    a.smallestDistancePair([1,3,1], 1)