# -*- coding: utf-8 -*-
# ======================================
# @File    : 436.py
# @Time    : 2020/11/25 9:47 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [436. 寻找右区间](https://leetcode-cn.com/problems/find-right-interval/)
    """
    @timeit
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        import heapq
        n = len(intervals)
        arr = [[intervals[i][0], intervals[i][1], i] for i in range(n)]
        arr.sort()
        pq = []
        res = [-1] * n
        for x, y, i in arr:
            while pq and pq[0][0] <= x:
                t = heapq.heappop(pq)
                res[t[-1]] = i
            heapq.heappush(pq, [y, x, i])
        return res

if __name__ == '__main__':
    a = Solution()
    a.findRightInterval([[1,2]])
    a.findRightInterval([[3,4], [2,3], [1,2]])
    a.findRightInterval([[1,4], [2,3], [3,4]])