# -*- coding: utf-8 -*-
# ======================================
# @File    : 922.py
# @Time    : 2020/11/12 1:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [922. 按奇偶排序数组 II](https://leetcode-cn.com/problems/sort-array-by-parity-ii/)
    """
    @timeit
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        i, j = 0, 1
        while i < n and j < n:
            while i < n and A[i] & 1 == 0:
                i += 2
            while j < n and A[j] & 1 == 1:
                j += 2
            if i < n and j < n:
                A[i], A[j] = A[j], A[i]
        return A

if __name__ == '__main__':
    a = Solution()
    a.sortArrayByParityII([4,2,5,7])