# -*- coding: utf-8 -*-
# ======================================
# @File    : 11.py
# @Time    : 2019/11/10 22:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def maxArea(self, height: List[int]) -> int:
        """
        [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)
        思路：双指针从两侧向中间，每次移动较小的一边
        """
        lo, hi = 0, len(height) - 1
        res = 0
        while lo < hi:
            if height[lo] < height[hi]:
                y = height[lo]
                lo += 1
            else:
                y = height[hi]
                hi -= 1
            res = max(res, y * (hi - lo + 1))
        return res


if __name__ == '__main__':
    a = Solution()
    a.maxArea([1,8,6,2,5,4,8,3,7])