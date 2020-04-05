# -*- coding: utf-8 -*-
# ======================================
# @File    : 5377.py
# @Time    : 2020/4/5 10:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5377. 将二进制表示减到 1 的步骤数]()
    """
    @timeit
    def numSteps(self, s: str) -> int:
        n = i = 0
        for c in s[::-1]:
            if c == '1':
                n += (1 << i)
            i += 1
        res = 0
        while n > 1:
            if n & 1:
                n += 1
            else:
                n //= 2
            res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.numSteps(s = "1101")
    a.numSteps(s = "10")
    a.numSteps(s = "1")