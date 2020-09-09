# -*- coding: utf-8 -*-
# ======================================
# @File    : 1577.py
# @Time    : 2020/9/9 12:58 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1577. 数的平方等于两数乘积的方法数](https://leetcode-cn.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/)
    """
    @timeit
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d1, d2 = {}, {}
        for x in nums1:
            d1[x] = d1.get(x, 0) + 1
        for x in nums2:
            d2[x] = d2.get(x, 0) + 1
        def f(d1, d2):
            res = 0
            for i, x in d1.items():
                for j, y in d1.items():
                    k = (i * j) ** 0.5
                    if k in d2:
                        if i == j:
                            res += x * (x-1) * d2[k]
                        else:
                            res += x * y * d2[k]
            return res
        return (f(d1, d2) + f(d2, d1)) // 2

if __name__ == '__main__':
    a = Solution()
    a.numTriplets(nums1 = [7,4], nums2 = [5,2,8,9])
    a.numTriplets(nums1 = [1,1], nums2 = [1,1,1])
    a.numTriplets(nums1 = [7,7,8,3], nums2 = [1,2,9,7])
    a.numTriplets(nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18])