# -*- coding: utf-8 -*-
# ======================================
# @File    : 1094.py
# @Time    : 2020/03/05 00:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1103. 分糖果 II](https://leetcode-cn.com/problems/distribute-candies-to-people/)
    1,2,3
    5,7,9
    15,18,21
    """
    @timeit
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        m, n = candies, num_people
        def f(n, s, p):
            e = s + (n - 1) * p
            return (s + e) * n // 2
        lo, hi = 1, m // n
        while lo < hi:
            # 第mid层
            mid = lo + (hi - lo) // 2
            st = f(mid, 1, n)
            if f(n, st, mid) < m:
                lo = mid + 1
            else:
                hi = mid
        s = f(lo-1, 1, n)
        res = [i*(lo-1) + s for i in range(n)]
        t = f(n, s, lo-1)
        m -= t
        ss = (lo-1) * n + 1
        i = 0
        while m > 0:
            res[i] += min(m, ss)
            i += 1
            m -= ss
            ss += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.distributeCandies(7,4)
    a.distributeCandies(10,3)
    a.distributeCandies(60,4)
