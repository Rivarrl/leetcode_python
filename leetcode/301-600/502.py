# -*- coding: utf-8 -*-
# ======================================
# @File    : 502.py
# @Time    : 2020/3/16 13:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [502. IPO](https://leetcode-cn.com/problems/ipo/)
    """
    @timeit
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        import heapq
        from functools import cmp_to_key
        if W > max(Capital): return sum(Profits)
        n = len(Profits)
        arr = [[Capital[i], Profits[i]] for i in range(n)]
        def cmp(x, y):
            if x[0] == y[0]:
                if x[1] < y[1]:
                    return 1
                else:
                    return -1
            if x[0] > y[0]:
                return 1
            else:
                return -1
        arr.sort(key=cmp_to_key(cmp))
        hp = []
        res = W
        for i in range(n):
            c, p = arr[i]
            if i >= k + 1:
                heapq.heappop(hp)
            res -= c
            if res < 0: break
            res += p
            heapq.heappush(hp, (p, c))

        return res - W if res - W > 0 else 0


if __name__ == '__main__':
    a = Solution()
    a.findMaximizedCapital(k=2, W=0, Profits=[1,2,3], Capital=[0,1,1])
