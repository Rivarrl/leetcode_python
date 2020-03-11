# -*- coding: utf-8 -*-
# ======================================
# @File    : 65.py
# @Time    : 2020/3/12 0:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# [面试题65. 不用加减乘除做加法](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)

class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xffffffff
        b &= 0xffffffff
        while b != 0:
            a, b = a^b, ((a&b) << 1) & 0xffffffff
        return a if a <= 0x7fffffff else ~(a ^ 0xffffffff)


if __name__ == '__main__':
    a = Solution()
    n=a.add(9, 5)
    print(n)