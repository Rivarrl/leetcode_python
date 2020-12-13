# -*- coding: utf-8 -*-
# ======================================
# @File    : 5611.py
# @Time    : 2020/12/12 23:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5611. 石子游戏 VI]()
    """
    @timeit
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        import heapq
        q1, q2 = [], []
        n = len(aliceValues)
        popped = [False] * n
        for i in range(n):
            a, b = aliceValues[i], bobValues[i]
            heapq.heappush(q1, [-(100 * (a+b) + a), i])
            heapq.heappush(q2, [-(100 * (a+b) + b), i])
        res = 0
        while q1 and q2:
            _, i = heapq.heappop(q1)
            while q1 and popped[i]:
                _, i = heapq.heappop(q1)
            if popped[i]: break
            popped[i] = True
            res += aliceValues[i]
            if not q2: break
            _, j = heapq.heappop(q2)
            while q2 and popped[j]:
                _, j = heapq.heappop(q2)
            if popped[j]: break
            popped[j] = True
            res -= bobValues[j]
        return res // abs(res) if res else 0


if __name__ == '__main__':
    a = Solution()
    a.stoneGameVI(aliceValues = [1,3], bobValues = [2,1])
    a.stoneGameVI(aliceValues = [1,2], bobValues = [3,1])
    a.stoneGameVI(aliceValues = [2,4,3], bobValues = [1,6,7])
    a.stoneGameVI([6,5,1,2,10,6], [7,7,7,7,3,7])
    a.stoneGameVI([9,8,3,8], [10,6,9,5])