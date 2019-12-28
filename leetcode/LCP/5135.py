# -*- coding: utf-8 -*-
# ======================================
# @File    : 5135.py
# @Time    : 2019/12/28 22:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5135. 转变数组后最接近目标值的数组和](https://leetcode-cn.com/contest/biweekly-contest-16/problems/sum-of-mutated-array-closest-to-target/)
    """
    @timeit
    def findBestValue(self, arr: List[int], target: int) -> int:
        import bisect
        arr.sort()
        n = len(arr)
        pre = [0]
        for e in arr:
            pre += [pre[-1] + e]
        def f(x):
            i = bisect.bisect_left(arr, x)
            return pre[i] + x * (n - i)
        lo, hi = 1, max(arr)
        while lo < hi:
            mid = lo + hi >> 1
            if f(mid) < target:
                lo = mid + 1
            else:
                hi = mid
        k1, k2 = abs(target - f(lo)), abs(target - f(lo - 1))
        return lo if k1 < k2 else lo - 1


if __name__ == '__main__':
    a = Solution()
    a.findBestValue(arr = [4,9,3], target = 10)
    a.findBestValue(arr = [2,3,5], target = 10)
    a.findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803)