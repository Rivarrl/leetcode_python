# -*- coding: utf-8 -*-
# ======================================
# @File    : 5171.py
# @Time    : 2020/2/23 11:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5171. 最接近的因数](https://leetcode-cn.com/problems/closest-divisors/)
    """
    @timeit
    def closestDivisors(self, num: int) -> List[int]:
        x, y = num + 1, num + 2
        k1 = x ** 0.5
        k2 = y ** 0.5
        if int(k1) == k1:
            return [int(k1), int(k1)]
        if int(k2) == k2:
            return [int(k2), int(k2)]
        ki2 = int(k2)
        for i in range(ki2, 0, -1):
            j = x / i
            r1, r2 = [], []
            if int(j) == j:
                r1 = [i, int(j)]
            k = y / i
            if int(k) == k:
                r2 = [i, int(k)]
            if r1 and r2:
                if abs(i - k) < abs(i - j):
                    return r2
                return r1
            elif r1:
                return r1
            elif r2:
                return r2



if __name__ == '__main__':
    a = Solution()
    a.closestDivisors(8)
    a.closestDivisors(123)
    a.closestDivisors(999)