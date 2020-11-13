# -*- coding: utf-8 -*-
# ======================================
# @File    : 1122.py
# @Time    : 2020/11/14 0:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1122. 数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array/)
    """
    @timeit
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        tail = []
        for i, x in enumerate(arr2):
            d[x] = 0
        for i, x in enumerate(arr1):
            if x in d:
                d[x] += 1
            else:
                tail.append(x)
        res = []
        for i, x in enumerate(arr2):
            res += [x] * d[x]
        tail.sort()
        return res + tail

if __name__ == '__main__':
    a = Solution()
    a.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])