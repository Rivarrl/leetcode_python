# -*- coding: utf-8 -*-
# ======================================
# @File    : 1413.py
# @Time    : 2020/4/24 13:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1413. 逐步求和得到正数的最小值](https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum/)
    """
    @timeit
    def minStartValue(self, nums: List[int]) -> int:
        res, k = 1, 0
        for e in nums:
            k += e
            res = max(res, 1-k)
        return res

if __name__ == '__main__':
    a = Solution()
    a.minStartValue([-3,2,-3,4,2])
    a.minStartValue(nums = [1,2])
    a.minStartValue(nums = [1,-2,-3])