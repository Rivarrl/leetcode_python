# -*- coding: utf-8 -*-
# ======================================
# @File    : 5359.py
# @Time    : 2020/3/15 10:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        import heapq
        arr = [[efficiency[i], speed[i]] for i in range(n)]
        arr.sort(reverse=True)
        p = []
        res = t = 0
        for i in range(n):
            e, s = arr[i]
            t += s
            heapq.heappush(p, s)
            if i >= k:
                t -= heapq.heappop(p)
            res = max(res, e * t)
        return res % (10**9+7)

if __name__ == '__main__':
    a = Solution()
    a.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2)
    a.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3)
    a.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4)