# -*- coding: utf-8 -*-
# ======================================
# @File    : 5308
# @Time    : 2020/1/12 13:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5308. 或运算的最小翻转次数]()
    """
    @timeit
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while c or a or b:
            da, db, dc = a & 1, b & 1, c & 1
            if dc != da | db:
                if dc == 1:
                    res += 1
                else:
                    res += int(dc != da) + int(dc != db)
            c >>= 1
            a >>= 1
            b >>= 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.minFlips(2,6,5)
    a.minFlips(4,2,7)
    a.minFlips(1,2,3)
    a.minFlips(8,3,5)