# -*- coding: utf-8 -*-
# ======================================
# @File    : 5349.py
# @Time    : 2020/3/21 23:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        d = {}
        for i, j in reservedSeats:
            if not i in d:
                d[i] = []
            d[i].append(j)
        res = 0
        def f(arr):
            for x in range(2, 10):
                if x in arr:
                    break
            else:
                return 2
            for x in range(2, 6):
                if x in arr:
                    break
            else:
                return 1
            for x in range(4, 8):
                if x in arr:
                    break
            else:
                return 1
            for x in range(6, 10):
                if x in arr:
                    break
            else:
                return 1
            return 0
        for i in sorted(d.keys()):
            res += f(d[i])
        res += (n - len(d)) * 2
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])
    a.maxNumberOfFamilies(n = 2, reservedSeats = [[2,1],[1,8],[2,6]])
    a.maxNumberOfFamilies(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]])
    a.maxNumberOfFamilies(5, [[4,7],[4,1],[3,1],[5,9],[4,4],[3,7],[1,3],[5,5],[1,6],[1,8],[3,9],[2,9],[1,4],[1,9],[1,10]])