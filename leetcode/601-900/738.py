# -*- coding: utf-8 -*-
# ======================================
# @File    : 738.py
# @Time    : 2020/12/15 0:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [738. 单调递增的数字](https://leetcode-cn.com/problems/monotone-increasing-digits/)
    """
    @timeit
    def monotoneIncreasingDigits(self, N: int) -> int:
        x = N
        last = 10
        res, tot = -1, 0
        while x:
            a = x % 10
            if a > last:
                res = (x - 1) * 10 ** tot + (10 ** tot - 1)
                a -= 1
            last = a
            tot += 1
            x //= 10
        return N if res == -1 else res

if __name__ == '__main__':
    a = Solution()
    a.monotoneIncreasingDigits(10)
    a.monotoneIncreasingDigits(1234)
    a.monotoneIncreasingDigits(332)