# -*- coding: utf-8 -*-
# ======================================
# @File    : 321.py
# @Time    : 2019/12/12 12:43
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [321. 拼接最大数](https://leetcode-cn.com/problems/create-maximum-number/)
    """
    @timeit
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        """
        思路: 用f(k)代表nums1和nums2的最长为k的最大拼接子序列,
        g(i, j)代表nums(i+1)的最长为j的最大拼接子序列,
        f(k) = g(0, k-x) + g(1, x)
        """
        import functools
        @functools.lru_cache(None)
        def g(t, j):
            nums = [nums1, nums2][t]
            # 需要pop的最多次数
            q = len(nums) - j
            stk = []
            for i in range(len(nums)):
                while q > 0 and stk and stk[-1] < nums[i]:
                    q -= 1
                    stk.pop()
                stk.append(nums[i])
            return stk[:j]

        def cmp_post(arr1, arr2, i=0, j=0):
            if j == len(arr2): return True
            if i == len(arr1): return False
            if arr1[i] == arr2[j]: return cmp_post(arr1, arr2, i + 1, j + 1)
            return arr1[i] > arr2[j]

        def f(arr1, arr2):
            i, j = 0, 0
            n, m = len(arr1), len(arr2)
            arr = [0] * (n + m)
            for p in range(m+n):
                if i == n:
                    arr[p] = arr2[j]
                    j += 1
                elif j == m:
                    arr[p] = arr1[i]
                    i += 1
                elif arr1[i] > arr2[j]:
                    arr[p] = arr1[i]
                    i += 1
                elif arr1[i] < arr2[j]:
                    arr[p] = arr2[j]
                    j += 1
                else:
                    if cmp_post(arr1, arr2, i, j):
                        arr[p] = arr1[i]
                        i += 1
                    else:
                        arr[p] = arr2[j]
                        j += 1
            return arr

        n, m = len(nums1), len(nums2)
        res = [0] * (m + n)
        for i in range(k+1):
            j = k - i
            if i > n or j > m: continue
            arr1, arr2 = g(0, i), g(1, j)
            cur = f(arr1, arr2)
            if cmp_post(cur, res):
                res = cur[:]
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxNumber(nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k=5)
    a.maxNumber(nums1 = [6, 7], nums2 = [6, 0, 4], k = 5)
    a.maxNumber(nums1 = [3, 9], nums2 = [8, 9], k = 3)
    a.maxNumber([6,7,5], [4,8,1], 3)