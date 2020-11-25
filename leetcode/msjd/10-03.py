# -*- coding: utf-8 -*-
# ======================================
# @File    : 10-03.py
# @Time    : 2020/11/25 12:45 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 10.03. 搜索旋转数组](https://leetcode-cn.com/problems/search-rotate-array-lcci/)
    """
    @timeit
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)
        def f(i):
            j = i
            while j > 0 and arr[j-1] == target:
                j -= 1
            while i != 0 and arr[(i+1) % n] == target:
                i = (i + 1) % n
            return min(i, j)
        lo, hi = 0, n - 1
        while lo < hi:
            mi = lo + hi >> 1
            if target == arr[mi]:
                lo = f(mi)
                break
            if target == arr[hi]:
                lo = f(hi)
                break
            if arr[mi] == arr[hi]:
                hi -= 1
            elif target < arr[mi] < arr[hi]:
                hi = mi - 1
            elif arr[mi] < target < arr[hi]:
                lo = mi + 1
            elif arr[mi] < arr[hi] < target:
                hi = mi - 1
            elif target > arr[mi] > arr[hi]:
                lo = mi + 1
            elif arr[mi] > target > arr[hi]:
                hi = mi - 1
            elif arr[mi] > arr[hi] > target:
                lo = mi + 1
        if arr[lo] == target: return lo
        return -1

if __name__ == '__main__':
    a = Solution()
    a.search(arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5)
    a.search(arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11)
    a.search([1,1,1,1,1,2,1,1,1], 2)
    a.search([5,5,5,1,2,3,4,5], 5)