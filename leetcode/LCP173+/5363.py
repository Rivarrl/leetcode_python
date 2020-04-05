# -*- coding: utf-8 -*-
# ======================================
# @File    : 5363.py
# @Time    : 2020/4/4 23:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5363. 做菜顺序](https://leetcode-cn.com/problems/reducing-dishes/)
    """
    @timeit
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if max(satisfaction) < 0: return 0
        satisfaction.sort()
        n = len(satisfaction)
        s = sum(satisfaction[i] * (i + 1) for i in range(n))
        p = sum(satisfaction)
        i = 0
        while s - p > s:
            s -= p
            p -= satisfaction[i]
            i += 1
        return s


if __name__ == '__main__':
    a = Solution()
    a.maxSatisfaction([-1,-8,0,5,-9])
    a.maxSatisfaction([4,3,2])
    a.maxSatisfaction([-1,-4,-5])
    a.maxSatisfaction([-2,5,-1,0,3,-3])
