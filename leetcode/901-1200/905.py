# -*- coding: utf-8 -*-
# ======================================
# @File    : 905.py
# @Time    : 2019/11/11 1:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        [905. 按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity/)
        思路：双指针找奇偶交换，与快排的partition方法相似
        """
        lo, hi = 0, len(A) - 1
        while lo < hi:
            while lo < hi and A[lo] % 2 == 0:
                lo += 1
            while lo < hi and A[hi] & 1 == 1:
                hi -= 1
            if lo < hi:
                A[hi], A[lo] = A[lo], A[hi]
                lo += 1
                hi -= 1
        return A

if __name__ == '__main__':
    a = Solution()
    a.sortArrayByParity([3,1,2,4])
    a.sortArrayByParity([0,2,1,4])
    a.sortArrayByParity([1,3,0,5])
    a.sortArrayByParity([0,2,1])
    a.sortArrayByParity([1,0,2])