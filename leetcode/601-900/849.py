# -*- coding: utf-8 -*-
# ======================================
# @File    : 849.py
# @Time    : 2020/4/23 23:19
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        a = [0] * n
        last = 0 if a[0] == 1 else -1
        for i in range(n):
            if seats[i] == 1:
                last = i
                a[i] = n
            else:
                a[i] = n if last == -1 else i - last
        last = n-1 if a[-1] == 1 else -1
        for i in range(n-1, -1, -1):
            if last == -1:
                pass
            else:
                a[i] = min(a[i], last - i)
            if seats[i] == 1:
                last = i
                a[i] = n
        for i in range(n):
            if a[i] == n:
                a[i] = -1
        return max(a)

if __name__ == '__main__':
    a = Solution()
    a.maxDistToClosest([1,0,0,0,1,0,1])
    a.maxDistToClosest([1,0,0,0])
    a.maxDistToClosest([0,0,1])