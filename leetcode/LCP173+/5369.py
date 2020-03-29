# -*- coding: utf-8 -*-
# ======================================
# @File    : 5369.py
# @Time    : 2020/3/29 10:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.numTeams(rating = [2,5,3,4,1])
    a.numTeams(rating = [2,1,3])
    a.numTeams(rating = [1,2,3,4])
