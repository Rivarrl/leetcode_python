# -*- coding: utf-8 -*-
# ======================================
# @File    : 5624.py
# @Time    : 2020/12/26 23:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5624. 得到连续 K 个 1 的最少相邻交换次数]()
    """
    @timeit
    def minMoves(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tot, lm = 0, 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1] == 1:
                tot += 1
            elif nums[i] == 1:
                tot = 1
            else:
                tot = 0
            lm = max(tot, lm)
        if lm >= k: return 0
        pre = [0]
        for i in range(n):
            pre += [pre[-1] + nums[i]]
        def f(x):
            h = pre[x]
            if h >= k: return True
            for i in range(x, n):
                h += nums[i] - nums[i-x]
                if h >= k: return True
            return False
        lo, hi = 1, n
        while lo < hi:
            mi = lo + hi >> 1
            if f(mi):
                hi = mi
            else:
                lo = mi + 1
        def count(i, j):

        res = 10 ** 10 + 1
        for i in range(lo-1, n):
            if pre[i+1] - pre[i+1-lo] >= k:
                res = min(res, count(i-lo+1, i))
        return res

if __name__ == '__main__':
    a = Solution()
    a.minMoves(nums = [1,0,0,1,0,1], k = 2)
    a.minMoves(nums = [1,0,0,0,0,0,1,1], k = 3)
    a.minMoves(nums = [1,1,0,1], k = 2)