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
        if W > max(Capital): return sum(heapq.nlargest(k, Profits)) + W
        n = len(Profits)
        arr = [[Capital[i], Profits[i]] for i in range(n)]
        arr.sort(key=lambda x:-x[0])
        hp = []
        for i in range(k):
            while arr and arr[-1][0] <= W:
                heapq.heappush(hp, -arr.pop()[1])
            if hp:
                W -= heapq.heappop(hp)
            else:
                break
        return W


if __name__ == '__main__':
    a = Solution()
    a.findMaximizedCapital(k=2, W=0, Profits=[1,2,3], Capital=[0,1,1])
    a.findMaximizedCapital(3,0,[1,2,3],[0,1,2])
