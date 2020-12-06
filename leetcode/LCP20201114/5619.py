# -*- coding: utf-8 -*-
# ======================================
# @File    : 5619.py
# @Time    : 2020/12/6 11:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5619. 最小不兼容性]()
    """
    @timeit
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        from collections import Counter
        from functools import lru_cache
        d = Counter(nums)
        if max(d.values()) > k: return -1
        n = len(nums)
        m = n // k
        nums.sort()
        def count1(x):
            res = 0
            while x:
                x &= (x-1)
                res += 1
            return res
        inf = (nums[-1] - nums[0]) * k + 1
        @lru_cache(None)
        def f(i, st):
            if i == n:
                return calc(st)
            res = inf
            st = list(st)
            for j in range(k):
                if count1(st[j]) == m: continue
                st[j] ^= (1 << i)
                res = min(res, f(i+1, tuple(st)))
                st[j] ^= (1 << i)
            return res
        def calc(st):
            res = 0
            for j in range(k):
                x = st[j]
                i = 0
                rec = []
                while x:
                    if x & 1:
                        rec.append(nums[i])
                    i += 1
                    x >>= 1
                if len(set(rec)) < m: return inf
                res += rec[-1] - rec[0]
            return res
        return f(0, tuple([0 for _ in range(k)]))


if __name__ == '__main__':
    a = Solution()
    a.minimumIncompatibility(nums = [1,2,1,4], k = 2)
    a.minimumIncompatibility(nums = [6,3,8,1,3,1,2,2], k = 4)
    a.minimumIncompatibility(nums = [5,3,3,6,3,3], k = 3)