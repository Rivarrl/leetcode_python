# -*- coding: utf-8 -*-
# ======================================
# @File    : 5350.py
# @Time    : 2020/3/21 23:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def cmp(x):
            z = x
            r = 0
            while z != 1:
                if z & 1:
                    z = z*3 + 1
                else:
                    z //= 2
                r += 1
            return r
        arr = [i for i in range(lo, hi+1)]
        arr.sort(key=cmp)
        return arr[k-1]


if __name__ == '__main__':
    a = Solution()
    a.getKth(lo = 12, hi = 15, k = 2)
    a.getKth(lo = 1, hi = 1, k = 1)
    a.getKth(lo = 7, hi = 11, k = 4)
    a.getKth(lo = 10, hi = 20, k = 5)
    a.getKth(lo = 1, hi = 1000, k = 777)