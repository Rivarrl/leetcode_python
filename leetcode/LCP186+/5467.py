# -*- coding: utf-8 -*-
# ======================================
# @File    : 5467.py
# @Time    : 2020/7/19 11:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def closestToTarget(self, arr: List[int], target: int) -> int:
        n = len(arr)
        for i in range(n):


if __name__ == '__main__':
    a = Solution()
    a.closestToTarget(arr = [9,12,3,7,15], target = 5)
    a.closestToTarget(arr = [1000000,1000000,1000000], target = 1)
    a.closestToTarget(arr = [1,2,4,8,16], target = 0)