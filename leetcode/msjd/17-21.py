# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-21.py
# @Time    : 2020/10/3 1:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.21. 直方图的水量](https://leetcode-cn.com/problems/volume-of-histogram-lcci/)
    """
    @timeit
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        hh = [[0, 0] for _ in range(n)]
        lh = rh = 0
        for i in range(n):
            j = n-1-i
            hh[i][0] = lh
            lh = max(lh, height[i])
            hh[j][1] = rh
            rh = max(rh, height[j])
        for i in range(n):
            res += max(min(hh[i][0], hh[i][1]) - height[i], 0)
        return res

if __name__ == '__main__':
    a = Solution()
    a.trap([0,1,0,2,1,0,1,3,2,1,2,1])