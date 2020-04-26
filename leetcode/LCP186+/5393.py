# -*- coding: utf-8 -*-
# ======================================
# @File    : 5393.py
# @Time    : 2020/4/26 15:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5393. 可获得的最大点数](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/)
    """
    @timeit
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre = [0]
        for p in cardPoints:
            pre += [pre[-1] + p]
        n = len(cardPoints)
        res = 0
        for i in range(k+1):
            j = i + n - k
            c = pre[-1] - (pre[j] - pre[i])
            res = max(res, c)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3)
    a.maxScore(cardPoints = [2,2,2], k = 2)
    a.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7)
    a.maxScore(cardPoints = [1,1000,1], k = 1)
    a.maxScore(cardPoints = [1,79,80,1,1,1,200,1], k = 3)
    a.maxScore([96,90,41,82,39,74,64,50,30], 8)