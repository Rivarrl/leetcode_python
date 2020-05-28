# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-14.py
# @Time    : 2020/5/27 19:22
# @Author  : Rivarrl
# ======================================
# [面试题 17.14. 最小K个数](https://leetcode-cn.com/problems/smallest-k-lcci/)
from algorithm_utils import *

class Solution:
    @timeit
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        res = [e for e in arr[:k]]
        def build(i):
            j = i
            l, r = j * 2 + 1, j * 2 + 2
            if l < k and res[j] < res[l]: j = l
            if r < k and res[j] < res[r]: j = r
            if j != i:
                res[j], res[i] = res[i], res[j]
                build(j)
        for i in range(k//2, -1, -1):
            build(i)
        n = len(arr)
        for i in range(k, n):
            if arr[i] < res[0]:
                res[0] = arr[i]
                build(0)
        return res

if __name__ == '__main__':
    a = Solution()
    a.smallestK([1,3,5,7,2,4,6,8], 4)