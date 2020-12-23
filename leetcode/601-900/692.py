# -*- coding: utf-8 -*-
# ======================================
# @File    : 692.py
# @Time    : 2020/12/23 9:46 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [692. 前K个高频单词](https://leetcode-cn.com/problems/top-k-frequent-words/)
    """
    @timeit
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        import heapq
        from functools import cmp_to_key
        ctr = Counter(words)
        q = []
        for x in ctr:
            heapq.heappush(q, (ctr[x], x))
        def str_cmp(x, y):
            i, j = 0, 0
            n, m = len(x), len(y)
            while i < n and j < m:
                if x[i] > y[i]: return -1
                elif x[i] < y[i]: return 1
                i += 1
                j += 1
            return 0 if n == m else (m - n) // abs(m - n)
        def cmp(x, y):
            if x[0] > y[0]: return 1
            elif x[0] < y[0]: return -1
            else:
                return str_cmp(x[1], y[1])
        return [e[1] for e in heapq.nlargest(k, q, key=cmp_to_key(cmp))]

if __name__ == '__main__':
    a = Solution()
    a.topKFrequent(["i", "love", "leetcode", "i", "love", "coding", "coding", "codings", "codings"], k = 2)
    a.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4)