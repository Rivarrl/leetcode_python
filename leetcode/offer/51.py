# -*- coding: utf-8 -*-
# ======================================
# @File    : 51.py
# @Time    : 2020/4/24 0:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        arr = [0] * n
        idx = [i for i in range(n)]
        res = 0
        def merge(lo, hi):
            nonlocal res
            if lo >= hi: return
            if lo + 1 == hi:
                if nums[lo] > nums[hi]:
                    nums[lo], nums[hi] = nums[hi], nums[lo]
                    res += 1
                return
            mi = lo + (hi - lo) // 2
            merge(lo, mi)
            merge(mi, hi)
            i, j, k = lo, mi, lo
            while i < mi or j <= hi:
                if i == mi:
                    x = j
                    j += 1
                elif j > hi:
                    x = i
                    i += 1
                elif nums[i] <= nums[j]:
                    x = i
                    i += 1
                else:
                    x = j
                    j += 1
                arr[k] = nums[x]
                idx[x] = k
                k += 1
            for i in range(lo, hi+1):
                if i > idx[i]: res += i - idx[i]
                nums[i] = arr[i]
        merge(0, n-1)
        return res

if __name__ == '__main__':
    a = Solution()
    # a.reversePairs([7,5,6,4])
    a.reversePairs([1,3,2,3,1])