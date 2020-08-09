# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-01.py
# @Time    : 2020/8/9 1:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.01. 不用加号的加法](https://leetcode-cn.com/problems/add-without-plus-lcci/)
    """
    @timeit
    def add(self, a: int, b: int) -> int:
        # 异或是无进位的加法运算，将a+b转为a^b+进位->(x+y)，递归至进位y为0时中止
        # python注意取mask
        mask = 1 << 32
        while b != 0:
            if b == mask:
                return a ^ (-mask)
            a, b = a^b, (a&b)<<1
        return a

if __name__ == '__main__':
    a = Solution()
    a.add(1, 1)
    a.add(-1, 2)
    a.add(111, 899)