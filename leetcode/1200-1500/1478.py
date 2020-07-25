# -*- coding: utf-8 -*-
# ======================================
# @File    : 1478.py
# @Time    : 2020/7/24 1:56 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        dp = [[0] * (k+1) for _ in range(n+1)]



if __name__ == '__main__':
    a = Solution()
    a.minDistance(houses = [1,4,8,10,20], k = 3)
    a.minDistance(houses = [2,3,5,12,18], k = 2)
    a.minDistance(houses = [7,4,6,1], k = 1)
    a.minDistance(houses = [3,6,14,10], k = 4)