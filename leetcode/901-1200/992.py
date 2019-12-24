# -*- coding: utf-8 -*-
# ======================================
# @File    : 992.py
# @Time    : 2019/12/23 20:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [992. K 个不同整数的子数组](https://leetcode-cn.com/problems/subarrays-with-k-different-integers/)
    双指针
    """
    @timeit
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        from collections import defaultdict
        i = j = 0
        n = len(A)
        d = defaultdict(int)
        def valid(d):
            return len([e for e in d if d[e] > 0]) == K
        res = 0
        while j < n:
            while j < n and not valid(d):
                d[A[j]] += 1
                j += 1
            res += 1
            while j < n and d[A[j]] > 0:
                d[A[j]] += 1
                res += 1
                j += 1
            while i < j and d[A[i]] > 0:
                d[A[i]] -= 1
                res += 1
                i += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.subarraysWithKDistinct(A = [1,2,1,2,3], K = 2)
    a.subarraysWithKDistinct(A = [1,2,1,3,4], K = 3)