# -*- coding: utf-8 -*-
# ======================================
# @File    : 40.py
# @Time    : 2020/3/20 10:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
# [面试题40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

class Solution:
    @timeit
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        def heapify(i):
            l, r = i * 2, i * 2 + 1
            x = i
            if l < n and arr[l] < arr[x]:
                x = l
            if r < n and arr[r] < arr[x]:
                x = r
            if x != i:
                arr[x], arr[i] = arr[i], arr[x]
                heapify(x)
        def build_heap():
            for i in range(n//2, -1, -1):
                heapify(i)
        build_heap()
        res = []
        for _ in range(k):
            res.append(arr[0])
            arr[0], arr[n-1] = arr[n-1], arr[0]
            n -= 1
            heapify(0)
        return res

if __name__ == '__main__':
    a = Solution()
    a.getLeastNumbers([3,2,1],2)
    a.getLeastNumbers([0,1,2,1],1)