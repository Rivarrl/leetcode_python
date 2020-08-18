# -*- coding: utf-8 -*-
# ======================================
# @File    : 05-07.py
# @Time    : 2020/8/17 18:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 05.07. 配对交换](https://leetcode-cn.com/problems/exchange-lcci/)
    """
    @timeit
    def exchangeBits(self, num: int) -> int:
        # 0xaaaaaaaa = 10101010101010101010101010101010
        # 0x55555555 = 1010101010101010101010101010101
        return ((0xaaaaaaaa & num) >> 1) | ((0x55555555 & num) << 1)

if __name__ == '__main__':
    a = Solution()
    a.exchangeBits(2)
    a.exchangeBits(3)