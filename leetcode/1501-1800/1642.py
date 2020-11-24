# -*- coding: utf-8 -*-
# ======================================
# @File    : 1642.py
# @Time    : 2020/11/25 0:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1642. 可以到达的最远建筑](https://leetcode-cn.com/problems/furthest-building-you-can-reach/)
    """
    @timeit
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # 优先队列，梯子用在差值最大的ladders个位置
        import heapq
        pq = []
        n = len(heights)
        need_bricks = 0
        for i in range(n-1):
            dh = heights[i+1] - heights[i]
            if dh > 0:
                heapq.heappush(pq, dh)
                if len(pq) > ladders:
                    need_bricks += heapq.heappop(pq)
                if need_bricks > bricks:
                    return i
        return n - 1

if __name__ == '__main__':
    a = Solution()
    a.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1)
    a.furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2)
    a.furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0)