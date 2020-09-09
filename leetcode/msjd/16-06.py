# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-06.py
# @Time    : 2020/9/9 22:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.06. 最小差](https://leetcode-cn.com/problems/smallest-difference-lcci/)
    """
    @timeit
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        from collections import Counter
        d1, d2 = Counter(a), Counter(b)
        c1, c2 = sorted(d1.keys()), sorted(d2.keys())
        n, m = len(c1), len(c2)
        i, j = 0, 0
        res = (1 << 31) - 1
        while i < n and j < m:
            res = min(res, abs(c1[i] - c2[j]))
            if c1[i] > c2[j]:
                j += 1
            else:
                i += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.smallestDifference([1,3,15,11,2], [23,127,235,19,8])