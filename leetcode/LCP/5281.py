# -*- coding: utf-8 -*-
# ======================================
# @File    : 5281.py
# @Time    : 2019/12/8 11:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5281. 使结果不超过阈值的最小除数
    """
    @timeit
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, sum(nums) + 1
        while lo < hi:
            mid = lo + hi >> 1
            if sum((e-1) // mid + 1 for e in nums) > threshold:
                lo = mid + 1
            else:
                hi = mid
        return lo

if __name__ == '__main__':
    a = Solution()
    a.smallestDivisor([1,2,5,9], 6)
    a.smallestDivisor([2,3,5,7,11], 11)
    a.smallestDivisor([19], 5)