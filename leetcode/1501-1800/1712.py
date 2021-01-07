# -*- coding: utf-8 -*-
# ======================================
# @File    : 1712.py
# @Time    : 2021/1/5 12:52
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1712. 将数组分成三个子数组的方案数](https://leetcode-cn.com/problems/ways-to-split-array-into-three-subarrays/)
    """
    @timeit
    def waysToSplit(self, nums: List[int]) -> int:
        pre = [0]
        for x in nums:
            pre.append(pre[-1] + x)
        n = len(nums)
        pm = (pre[-1] // 3) + (pre[-1] % 3)
        res = 0
        for i in range(1, n):
            a = pre[i]
            if a > pm: break
            lo, hi = i + 1, n
            while lo < hi:
                mi = lo + hi >> 1
                b = pre[mi] - pre[i]
                c = pre[-1] - pre[mi]
                if b > c:
                    hi = mi
                elif b < a:
                    lo = mi + 1
                else:
                    if hi == mi: break
                    hi = mi
            l = hi

            lo, hi = i + 1, n
            while lo < hi:
                mi = lo + hi >> 1
                b = pre[mi] - pre[i]
                c = pre[-1] - pre[mi]
                if b > c:
                    hi = mi
                elif b < a:
                    lo = mi + 1
                else:
                    if lo == mi: break
                    lo = mi
            r = lo
            res += r - l + 1
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    a = Solution()
    a.waysToSplit(nums = [1,1,1])
    a.waysToSplit(nums = [1,2,2,2,5,0])
    a.waysToSplit(nums = [3,2,1])
    a.waysToSplit([0, 3, 3])