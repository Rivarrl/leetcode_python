# -*- coding: utf-8 -*-
# ======================================
# @File    : 1611.py
# @Time    : 2020/10/28 1:41 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1611. 使整数变为 0 的最少操作次数](https://leetcode-cn.com/problems/minimum-one-bit-operations-to-make-integers-zero/)
    """
    @timeit
    def minimumOneBitOperations(self, n: int) -> int:
        # 格雷码的解码运算，编码为Gray(n) = n ^ (n >> 1)
        res = n
        while n >> 1:
            res ^= (n >> 1)
            n >>= 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.minimumOneBitOperations(n = 0)
    a.minimumOneBitOperations(n = 3)
    a.minimumOneBitOperations(n = 6)
    a.minimumOneBitOperations(n = 9)
    a.minimumOneBitOperations(n = 333)