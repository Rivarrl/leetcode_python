# -*- coding: utf-8 -*-
# ======================================
# @File    : 47.py
# @Time    : 2020/9/18 0:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        def f(j):
            if j == n: return [[]]
            res = []
            for x in f(j+1):
                for i in range(len(x) + 1):
                    res.append(x[:i] + [nums[j]] + x[i:])
            return [list(e) for e in set([tuple(e) for e in res])]
        return f(0)

if __name__ == '__main__':
    a = Solution()
    a.permuteUnique([1,1,2])