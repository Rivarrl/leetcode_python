# -*- coding: utf-8 -*-
# ======================================
# @File    : 5155.py
# @Time    : 1/25/20 10:31 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5155. 数组序号转换](https://leetcode-cn.com/problems/rank-transform-of-an-array/)
    """
    @timeit
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        d = {}
        arr1 = arr[:]
        arr1.sort()
        last = -(10**9 + 1)
        j = 0
        for i in range(n):
            e = arr1[i]
            if e > last:
                j += 1
                d[arr1[i]] = j
                last = e
        for i in range(n):
            arr[i] = d[arr[i]]
        return arr

if __name__ == '__main__':
    a = Solution()
    a.arrayRankTransform([40,10,20,30])
    a.arrayRankTransform([100,100,100])
    a.arrayRankTransform([-43])