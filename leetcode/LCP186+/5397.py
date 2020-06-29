# -*- coding: utf-8 -*-
# ======================================
# @File    : 5397.py
# @Time    : 2020/5/16 22:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5397. 最简分数](https://leetcode-cn.com/problems/simplified-fractions)
    """
    @timeit
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y):
            if x == 0: return y
            return gcd(y%x, x)
        res = []
        for b in range(2, n+1):
            for a in range(1, b):
                c = gcd(a, b)
                if a > 1 and c > 1 and gcd(c, a) > 1: continue
                res.append('{}/{}'.format(a, b))
        return res

if __name__ == '__main__':
    a = Solution()
    a.simplifiedFractions(2)
    a.simplifiedFractions(3)
    a.simplifiedFractions(4)
    a.simplifiedFractions(1)
    a.simplifiedFractions(6)