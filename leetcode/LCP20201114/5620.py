# -*- coding: utf-8 -*-
# ======================================
# @File    : 5620.py
# @Time    : 2020/12/6 10:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5620. 连接连续二进制数字]()
    """
    @timeit
    def concatenatedBinary(self, n: int) -> int:
        def bit(x):
            res = 0
            while x:
                x >>= 1
                res += 1
            return res
        m = 10**9+7
        res = 0
        for i in range(1, n+1):
            res = ((res << bit(i)) + i) % m
        return res

if __name__ == '__main__':
    a = Solution()
    a.concatenatedBinary(1)
    a.concatenatedBinary(3)
    a.concatenatedBinary(12)
    a.concatenatedBinary(16)
    a.concatenatedBinary(100000)