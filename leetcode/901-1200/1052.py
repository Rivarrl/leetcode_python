# -*- coding: utf-8 -*-
# ======================================
# @File    : 1052
# @Time    : 2021/2/23 16:13
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1052. 爱生气的书店老板](https://leetcode-cn.com/problems/grumpy-bookstore-owner/)
    """
    @timeit
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        if X >= n: return sum(customers)
        r = h = s = 0
        for i in range(n):
            h += customers[i] * grumpy[i]
            s += customers[i] * (1-grumpy[i])
            if i >= X:
                h -= customers[i-X] * grumpy[i-X]
            r = max(r, h)
        return s + r

if __name__ == '__main__':
    a = Solution()
    a.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3)
    a.maxSatisfied([4,10,10],[1,1,0],2)