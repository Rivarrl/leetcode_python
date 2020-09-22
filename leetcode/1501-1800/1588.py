# -*- coding: utf-8 -*-
# ======================================
# @File    : 1588.py
# @Time    : 2020/9/21 1:18 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1588. 所有奇数长度子数组的和](https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/)
    """
    @timeit
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            ocl, ecl = (i+1)//2, i//2+1
            ocr, ecr = (n-i)//2, (n-1-i)//2 + 1
            res += (ocl * ocr + ecl * ecr) * arr[i]
        return res

if __name__ == '__main__':
    a = Solution()
    a.sumOddLengthSubarrays([1,4,2,5,3])
    a.sumOddLengthSubarrays([1,2])
    a.sumOddLengthSubarrays([10,11,12])