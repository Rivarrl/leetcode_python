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
        def f(i, j):
            a = pre[i]
            b = pre[j] - pre[i]
            c = pre[-1] - pre[j]
            if a <= b <= c: return 1
            if a > b: return -1
            return 0

        res = 0
        for i in range(1, n-1):
            lo, hi = i + 1, n
            flag = False
            while lo < hi:
                mi = lo + hi >> 1
                st = f(i, mi)
            if flag:
                res += hi - i
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    a = Solution()
    a.waysToSplit(nums = [1,1,1])
    a.waysToSplit(nums = [1,2,2,2,5,0])
    a.waysToSplit(nums = [3,2,1])