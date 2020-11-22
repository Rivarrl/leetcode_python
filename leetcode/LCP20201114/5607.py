# -*- coding: utf-8 -*-
# ======================================
# @File    : 5607.py
# @Time    : 2020/11/22 11:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def waysToMakeFair(self, nums: List[int]) -> int:
        pre0 = [0]
        pre1 = [0]
        tot = 0
        for i, x in enumerate(nums):
            if i & 1:
                pre1 += [pre1[-1] + x]
            else:
                pre0 += [pre0[-1] + x]
            tot += x
        res = 0
        for i, x in enumerate(nums):
            if tot - x & 1: continue
            if i & 1:
                j = i // 2 + 1
                if pre0[j] + pre1[-1] - pre1[j] == (tot - x) // 2:
                    res += 1
            else:
                j = i // 2 + 1
                if pre1[j-1] + pre0[-1] - pre0[j] == (tot - x) // 2:
                    res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.waysToMakeFair(nums = [2,1,6,4])
    a.waysToMakeFair(nums = [1,1,1])
    a.waysToMakeFair(nums = [1,2,3])