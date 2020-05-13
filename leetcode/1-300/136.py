# -*- coding: utf-8 -*-
# ======================================
# @File    : 136.py
# @Time    : 2020/5/14 0:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x
        return res

if __name__ == '__main__':
    a = Solution()
    a.singleNumber([2,2,1])
    a.singleNumber([4,1,2,1,2])