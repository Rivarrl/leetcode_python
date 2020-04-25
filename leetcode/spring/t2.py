# -*- coding: utf-8 -*-
# ======================================
# @File    : t2.py
# @Time    : 2020/4/25 15:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minTime(self, time: List[int], m: int) -> int:
        def judge(x):
            # 最小为x的时候，能不能分m块
            c = k = 0
            p = 1
            for t in time:
                c += t
                k = max(k, t)
                if c - k > x:
                    c = k = t
                    p += 1
                if p > m:
                    return False
            return True
        if len(time) <= m: return 0
        lo, hi = 0, sum(time)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if judge(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo

if __name__ == '__main__':
    a = Solution()
    a.minTime([1,2,3,3], 2)
    a.minTime([999,999,999], 4)
    a.minTime([1,2,10,9,8,7,6,5,9,10], 5)
    a.minTime([1,1,2,2,1,3], 3)