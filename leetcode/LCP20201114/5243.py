# -*- coding: utf-8 -*-
# ======================================
# @File    : 5243.py
# @Time    : 2021/1/17 10:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1726. 同积元组](https://leetcode-cn.com/contest/weekly-contest-224/problems/tuple-with-same-product/)
    """
    @timeit
    def tupleSameProduct(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            for j in range(i):
                d[nums[i] * nums[j]] += 1
        res = 0
        for k in d:
            res += d[k] * (d[k] - 1) // 2
        return res * 8


if __name__ == '__main__':
    a = Solution()
    a.tupleSameProduct(nums = [2,3,4,6])
    a.tupleSameProduct(nums = [1,2,4,5,10])
    a.tupleSameProduct(nums = [2,3,4,6,8,12])
    a.tupleSameProduct(nums = [2,3,5,7])