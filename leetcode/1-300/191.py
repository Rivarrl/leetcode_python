# -*- coding: utf-8 -*-
# ======================================
# @File    : 191.py
# @Time    : 2020/4/21 15:48
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.hammingWeight(11)