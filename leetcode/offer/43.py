# -*- coding: utf-8 -*-
# ======================================
# @File    : 43.py
# @Time    : 2020/5/5 2:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def countDigitOne(self, n: int) -> int:
        res, i = 0, 1
        while i <= n:
            high = n // (10 * i)
            cur = (n // i) % 10
            low = n - (n // i) * i
            if cur == 0:
                res += high * i
            elif cur == 1:
                res += high * i + low + 1
            else:
                res += (high + 1) * i
            i *= 10
        return res

if __name__ == '__main__':
    a = Solution()
    a.countDigitOne(12)
    a.countDigitOne(13)