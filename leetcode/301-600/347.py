# -*- coding: utf-8 -*-
# ======================================
# @File    : 347.py
# @Time    : 2020/5/8 17:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)
    """
    @timeit
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        d = {}
        for e in nums:
            d[e] = d.get(e, 0) + 1
        q = []
        for key, value in d.items():
            heapq.heappush(q, (value, key))
        return [e[1] for e in heapq.nlargest(k, q)]

    @timeit
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        arr = [[-1, None] for _ in range(k)]
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        def sift(i):
            j = i
            l, r = j * 2 + 1, j * 2 + 2
            if l < k and arr[l][0] < arr[j][0]:
                j = l
            if r < k and arr[r][0] < arr[j][0]:
                j = r
            if i != j:
                swap(arr, i, j)
                sift(j)
        d = {}
        for e in nums:
            d[e] = d.get(e, 0) + 1
        for key, val in d.items():
            if arr[0][0] < val:
                arr[0] = [val, key]
                sift(0)
        return [e[1] for e in arr if e[0] != -1]

if __name__ == '__main__':
    a = Solution()
    a.topKFrequent2([1,1,1,2,2,3],2)
    a.topKFrequent2([1], 1)