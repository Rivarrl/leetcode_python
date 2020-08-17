# -*- coding: utf-8 -*-
# ======================================
# @File    : 05-06.py
# @Time    : 2020/8/17 19:10
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 05.06. 整数转换](https://leetcode-cn.com/problems/convert-integer-lcci/)
    """
    @timeit
    def convertInteger(self, A: int, B: int) -> int:
        mask = 0xffffffff
        c = A ^ B
        res = 0
        while c:
            if c < -mask: break
            c &= (c - 1)
            res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.convertInteger(29, 15)
    a.convertInteger(1, 2)
    a.convertInteger(826966453, -729934991)