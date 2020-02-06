# -*- coding: utf-8 -*-
# ======================================
# @File    : 5329.py
# @Time    : 2020/2/2 10:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1342. 数组大小减半](https://leetcode-cn.com/problems/reduce-array-size-to-the-half/)
    """
    @timeit
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        import heapq
        ctr = Counter(arr)
        n = len(arr)
        p = 0
        c = 0
        a = [[-v, k] for k, v in ctr.items()]
        heapq.heapify(a)
        while p < n // 2:
            e = heapq.heappop(a)
            p -= e[0]
            c += 1
        return c


if __name__ == '__main__':
    a = Solution()
    # a.minSetSize(arr = [3,3,3,3,5,5,5,2,2,7])
    # a.minSetSize(arr = [7,7,7,7,7,7])
    # a.minSetSize(arr = [1,9])
    # a.minSetSize(arr = [1000,1000,3,7])
    # a.minSetSize(arr = [1,2,3,4,5,6,7,8,9,10])
    a.minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19])