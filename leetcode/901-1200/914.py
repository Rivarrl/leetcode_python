# -*- coding: utf-8 -*-
# ======================================
# @File    : 914.py
# @Time    : 2020/3/27 0:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = {}
        for card in deck:
            d[card] = d.get(card, 0) + 1
        def gcd(x, y):
            if x == 0: return y
            return gcd(y%x, x)
        dv = list(set(d.values()))
        c = dv[0]
        for v in dv[1:]:
            c = gcd(c, v)
        return c != 1


if __name__ == '__main__':
    a = Solution()
    a.hasGroupsSizeX([1,2,3,4,4,3,2,1])
    a.hasGroupsSizeX([1,1,1,2,2,2,3,3])
    a.hasGroupsSizeX([1])
    a.hasGroupsSizeX([1,1])
    a.hasGroupsSizeX([1,1,2,2,2,2])