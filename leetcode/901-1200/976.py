# -*- coding: utf-8 -*-
# ======================================
# @File    : 976.py
# @Time    : 2019/12/13 23:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [976. 三角形的最大周长](https://leetcode-cn.com/problems/largest-perimeter-triangle/)
    """
    @timeit
    def largestPerimeter(self, A: List[int]) -> int:
        """
        思路：贪心，从最大的三条边开始尝试
        """
        A.sort()
        n = len(A)
        for i in range(n-1, 1, -1):
            if A[i] < A[i-1] + A[i-2]:
                return A[i] + A[i-1] + A[i-2]
        return 0


if __name__ == '__main__':
    a = Solution()
    a.largestPerimeter([2,1,2])
    a.largestPerimeter([1,2,1])
    a.largestPerimeter([3,2,3,4])
    a.largestPerimeter([3,6,2,3])