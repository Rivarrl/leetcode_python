# -*- coding: utf-8 -*-
# ======================================
# @File    : 5419.py
# @Time    : 2020/5/24 10:48
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
class Solution:
    @timeit
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        from functools import lru_cache
        n, m = len(nums1), len(nums2)
        @lru_cache(None)
        def dfs(i, j):
            if i == n or j == m: return 0
            plus = max(0, nums1[i] * nums2[j])
            a, b, c = dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1) + plus
            return max(a, b, c)
        res = dfs(0, 0)
        if res == 0:
            r = -(1 << 31)
            for a in nums1:
                for b in nums2:
                    r = max(r, a * b)
            return r
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6])
    a.maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7])
    a.maxDotProduct(nums1 = [-1,-1], nums2 = [1,1])