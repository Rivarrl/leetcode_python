# -*- coding: utf-8 -*-
# ======================================
# @File    : 201.py
# @Time    : 2020/8/23 23:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [201. 数字范围按位与](https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/)
    """
    @timeit
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n &= (n-1)
        return n


if __name__ == '__main__':
    a = Solution()
    a.rangeBitwiseAnd([5,7])
    a.rangeBitwiseAnd([0,1])