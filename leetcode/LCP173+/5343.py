# -*- coding: utf-8 -*-
# ======================================
# @File    : 5343.py
# @Time    : 2020/2/16 11:19
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5343. 多次求和构造目标数组](https://leetcode-cn.com/problems/construct-target-array-with-multiple-sums/)
    """
    @timeit
    def isPossible(self, target: List[int]) -> bool:
        import heapq
        t = [-e for e in target]
        n = len(target)
        s = sum(target)
        heapq.heapify(t)
        while t != [-1] * n:
            x = -heapq.heappop(t)
            nx = x - (s - x)
            s -= (x - nx)
            if s < 0 or nx <= 0:
                return False
            else:
                heapq.heappush(t, -nx)
        return True

if __name__ == '__main__':
    a = Solution()
    a.isPossible([9,3,5])
    a.isPossible([1,1,1,2])
    a.isPossible([8,5])
    a.isPossible([5,2])