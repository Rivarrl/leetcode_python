# -*- coding: utf-8 -*-
# ======================================
# @File    : 378.py
# @Time    : 2020/7/2 22:42
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [378. 有序矩阵中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)
    """
    @timeit
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def f(x):
            ctr, j = 0, n-1
            for i in range(n):
                while j >= 0 and matrix[i][j] > x:
                    j -= 1
                ctr += j + 1
            return ctr

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return -1
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if f(mi) < k:
                lo = mi + 1
            else:
                hi = mi
        return lo


if __name__ == '__main__':
    a = Solution()
    a.kthSmallest(matrix = [[ 1,  5,  9],
                           [10, 11, 13],
                           [12, 13, 15]], k = 8)