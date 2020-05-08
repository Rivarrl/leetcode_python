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

if __name__ == '__main__':
    a = Solution()
    a.topKFrequent([1,1,1,2,2,3],2)
    a.topKFrequent([1], 1)