# -*- coding: utf-8 -*-
# ======================================
# @File    : 2.py
# @Time    : 2020/9/12 15:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        import bisect
        mod = 10 ** 9 + 7
        staple.sort()
        drinks.sort()
        res = 0
        for i in range(len(staple)):
            lo = bisect.bisect_right(drinks, x-staple[i])
            res += lo
        return res % mod


if __name__ == '__main__':
    a = Solution()
    a.breakfastNumber(staple = [10,20,5], drinks = [5,5,2], x = 15)
    a.breakfastNumber(staple = [2,1,1], drinks = [8,9,5,1], x = 9)