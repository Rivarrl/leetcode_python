# -*- coding: utf-8 -*-
# ======================================
# @File    : 1583.py
# @Time    : 2020/9/14 21:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:


if __name__ == '__main__':
    a = Solution()
    a.unhappyFriends(n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]])
    a.unhappyFriends(n = 2, preferences = [[1], [0]], pairs = [[1, 0]])
    a.unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]])