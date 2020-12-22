# -*- coding: utf-8 -*-
# ======================================
# @File    : 668.py
# @Time    : 2020/12/22 9:42 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [668. 乘法表中第k小的数](https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/)
    """
    @timeit
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            res = 0
            row, col = 1, n
            while row <= m and col >= 1:
                if row * col <= x:
                    res += col
                    row += 1
                else:
                    col -= 1
            return res
        lo, hi = 1, m * n
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if count(mi) >= k:
                hi = mi
            else:
                lo = mi + 1
        return lo


if __name__ == '__main__':
    a = Solution()
    a.findKthNumber(m = 3, n = 3, k = 5)
    a.findKthNumber(m = 2, n = 3, k = 6)
    a.findKthNumber(3, 1, 3)