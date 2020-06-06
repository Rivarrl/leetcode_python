# -*- coding: utf-8 -*-
# ======================================
# @File    : 128.py
# @Time    : 2020/6/6 8:13
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [128. 最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/)
    """
    @timeit
    def longestConsecutive(self, nums: List[int]) -> int:
        # 记录每个值最为边界的最长连续序列数
        d = {}
        res = 0
        for x in nums:
            if not x in d:
                l, r = d.get(x-1, 0), d.get(x+1, 0)
                c = l + r + 1
                res = max(res, c)
                d[x] = d[x-l] = d[x+r] = c
        return res

if __name__ == '__main__':
    a = Solution()
    # a.longestConsecutive([100,4,200,1,3,2])
    a.longestConsecutive([1,2,0,1])