# -*- coding: utf-8 -*-
# ======================================
# @File    : 349.py
# @Time    : 2020/11/2 0:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    a = Solution()
    a.intersection(nums1 = [1,2,2,1], nums2 = [2,2])
    a.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])