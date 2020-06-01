# -*- coding: utf-8 -*-
# ======================================
# @File    : 1464.py
# @Time    : 2020/6/1 18:19
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1464. 数组中两元素的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array/)
    """
    @timeit
    def maxProduct(self, nums: List[int]) -> int:
        a = b = 1
        for x in nums:
            if x > a:
                b = a
                a = x
            elif x > b:
                b = x
        return (a-1) * (b-1)

if __name__ == '__main__':
    a = Solution()
    a.maxProduct([3,4,5,2])
    a.maxProduct([1,5,4,5])
    a.maxProduct([3,7])