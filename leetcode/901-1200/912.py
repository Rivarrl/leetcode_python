# -*- coding: utf-8 -*-
# ======================================
# @File    : 912.py
# @Time    : 2020/3/31 0:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(arr, i, j):
            if i >= j: return
            base = arr[i]
            l, r = i, j
            while l < r:
                while l < r and arr[r] > base:
                    r -= 1
                while l < r and arr[l] <= base:
                    l += 1
                arr[l], arr[r] = arr[r], arr[l]
            arr[i], arr[r] = arr[r], arr[i]
            quick_sort(arr, i, l-1)
            quick_sort(arr, l+1, j)
        quick_sort(nums, 0, len(nums)-1)
        return nums

if __name__ == '__main__':
    a = Solution()
    a.sortArray([5,2,3,1])
    a.sortArray([5,1,1,2,0,0])