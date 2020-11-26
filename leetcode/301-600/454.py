# -*- coding: utf-8 -*-
# ======================================
# @File    : 454.py
# @Time    : 2020/11/27 0:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [454. 四数相加 II](https://leetcode-cn.com/problems/4sum-ii/)
    """
    @timeit
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = 0
        e = dict()
        for a in A:
            for b in B:
                e[a + b] = e.get(a + b, 0) + 1
        for c in C:
            for d in D:
                s = -(c + d)
                if s in e:
                    n += e[s]
        return n

if __name__ == '__main__':
    a = Solution()
    a.fourSumCount(A = [ 1, 2],
B = [-2,-1],
C = [-1, 2],
D = [ 0, 2])