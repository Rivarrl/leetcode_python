# -*- coding: utf-8 -*-
# ======================================
# @File    : 941.py
# @Time    : 2020/4/20 21:19
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [941. 有效的山脉数组](https://leetcode-cn.com/problems/valid-mountain-array/)
    """
    @timeit
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3: return False
        i, n = 1, len(A)
        while i < n and A[i-1] < A[i]:
            i += 1
        if i == 1 or i == n: return False
        while i < n and A[i-1] > A[i]:
            i += 1
        return i == n

if __name__ == '__main__':
    a = Solution()
    a.validMountainArray([2,1])
    a.validMountainArray([3,5,5])
    a.validMountainArray([0,3,2,1])
    a.validMountainArray([0,2,3,3,5,2,1,0])