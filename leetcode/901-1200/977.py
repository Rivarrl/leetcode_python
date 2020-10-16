# -*- coding: utf-8 -*-
# ======================================
# @File    : 977.py
# @Time    : 2020/10/16 1:01 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [977. 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)
    """
    @timeit
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        i, j = 0, n - 1
        res = [0] * n
        for k in range(n-1, -1, -1):
            if A[j] + A[i] >= 0:
                res[k] = A[j] ** 2
                j -= 1
            else:
                res[k] = A[i] ** 2
                i += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.sortedSquares([-4,-1,0,3,10])
    a.sortedSquares([-7,-3,2,3,11])