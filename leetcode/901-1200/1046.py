# -*- coding: utf-8 -*-
# ======================================
# @File    : 1046.py
# @Time    : 2020/12/30 0:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1046. 最后一块石头的重量](https://leetcode-cn.com/problems/last-stone-weight/)
    """
    @timeit
    def lastStoneWeight(self, stones: List[int]) -> int:
        import bisect
        stones.sort()
        while len(stones) > 1:
            x, y = stones.pop(), stones.pop()
            bisect.insort_left(stones, x-y)
        return stones[0]

if __name__ == '__main__':
    a = Solution()
    a.lastStoneWeight([2,7,4,1,8,1])