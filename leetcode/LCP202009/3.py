# -*- coding: utf-8 -*-
# ======================================
# @File    : 3.py
# @Time    : 2020/9/12 15:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        r, ry, ryr = 0, 0x3f3f3f3f, 0x3f3f3f3f
        for i in range(n):
            c = int(leaves[i] != 'r')
            if i == 0:
                r = c
            else:
                r, ry, ryr = r + c, min(r, ry) + (c^1), min(ry, ryr) + c
        return ryr

if __name__ == '__main__':
    a = Solution()
    # a.minimumOperations(leaves = "rrryyyrryyyrr")
    # a.minimumOperations(leaves = "ryr")
    a.minimumOperations("yry")