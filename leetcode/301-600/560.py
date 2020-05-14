# -*- coding: utf-8 -*-
# ======================================
# @File    : 560.py
# @Time    : 2020/5/15 0:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [560. 和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k/)
    """
    @timeit
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        res = c = 0
        for x in nums:
            c += x
            if c - k in d: res += d[c-k]
            d[c] = d.get(c, 0) + 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.subarraySum([1,1,1], 2)
    a.subarraySum([1,2,3], 3)
    a.subarraySum([1,2,1,2,1], 3)