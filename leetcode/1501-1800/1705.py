# -*- coding: utf-8 -*-
# ======================================
# @File    : 1705.py
# @Time    : 2021/1/11 18:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1705. 吃苹果的最大数目](https://leetcode-cn.com/problems/maximum-number-of-eaten-apples/)
    """
    @timeit
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        q = []
        n = len(apples)
        res = 0
        for i in range(n):
            while q and q[0][0] < i:
                heapq.heappop(q)
            if apples[i] > 0:
                heapq.heappush(q, [i + days[i] - 1, apples[i]])
            if q:
                t = heapq.heappop(q)
                res += 1
                t[1] -= 1
                if t[1] > 0:
                    heapq.heappush(q, t)
        last_day = n - 1
        while q:
            t = heapq.heappop(q)
            if last_day < t[0]:
                if t[0] - last_day >= t[1]:
                    res += t[1]
                    last_day += t[1]
                else:
                    res += t[0] - last_day
                    last_day = t[0]
        return res

if __name__ == '__main__':
    a = Solution()
    a.eatenApples(apples = [1,2,3,5,2], days = [3,2,1,4,2])
    a.eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2])