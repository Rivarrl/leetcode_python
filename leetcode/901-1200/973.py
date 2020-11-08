# -*- coding: utf-8 -*-
# ======================================
# @File    : 973.py
# @Time    : 2020/11/9 0:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [973. 最接近原点的 K 个点](https://leetcode-cn.com/problems/k-closest-points-to-origin/)
    """
    @timeit
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        q = []
        for x, y in points:
            heapq.heappush(q, [x*x+y*y, [x, y]])
        return [e[1] for e in heapq.nsmallest(K, q)]

if __name__ == '__main__':
    a = Solution()
    a.kClosest(points = [[1,3],[-2,2]], K = 1)
    a.kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2)
