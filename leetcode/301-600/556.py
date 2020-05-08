# -*- coding: utf-8 -*-
# ======================================
# @File    : 556.py
# @Time    : 2020/5/8 21:45
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [556. 下一个更大元素 III](https://leetcode-cn.com/problems/next-greater-element-iii/)
    """
    @timeit
    def nextGreaterElement(self, n: int) -> int:
        arr = [int(e) for e in str(n)]
        i = len(arr) - 1
        while i > 0 and arr[i] <= arr[i - 1]: i -= 1
        if i == 0: return -1
        m, k = 1 << 31, 0
        for j in range(i, len(arr)):
            if arr[i-1] < arr[j] < m:
                m, k = arr[j], j
        arr[k], arr[i-1] = arr[i-1], arr[k]
        while k < len(arr) - 1 and arr[k] < arr[k+1]:
            arr[k], arr[k+1] = arr[k+1], arr[k]
            k += 1
        res = int(''.join([str(e) for e in arr[:i]+arr[i:][::-1]]))
        return res if res < (1 << 31) else -1

if __name__ == '__main__':
    a = Solution()
    # a.nextGreaterElement(12)
    # a.nextGreaterElement(21)
    a.nextGreaterElement(230241)
    a.nextGreaterElement(12443322)