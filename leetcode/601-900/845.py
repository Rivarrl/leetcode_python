# -*- coding: utf-8 -*-
# ======================================
# @File    : 845.py
# @Time    : 2020/10/25 9:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [845. 数组中的最长山脉](https://leetcode-cn.com/problems/longest-mountain-in-array/)
    """
    @timeit
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        up, down = [0] * n, [0] * n
        l = r = -1
        res = x = y = 0
        for i in range(n):
            j = n - 1 - i
            x = 1 if A[i] <= l else x + 1
            y = 1 if A[j] <= r else y + 1
            up[i], down[j] = x, y
            l, r = A[i], A[j]
        for i in range(n):
            if up[i] > 1 and down[i] > 1:
                res = max(res, up[i] + down[i] - 1)
        return res

if __name__ == '__main__':
    a = Solution()
    a.longestMountain([2,1,4,7,3,2,5])
    a.longestMountain([2,2,2])
    a.longestMountain([0,1,2,3,4,5,6,7,8,9])