# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-24.py
# @Time    : 2020/11/18 12:44 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.24. 数对和](https://leetcode-cn.com/problems/pairs-with-sum-lcci/)
    """
    @timeit
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        d = {}
        for x in nums:
            y = target - x
            if y in d and d[y] >= 1:
                d[y] -= 1
                res.append([x, y])
            else:
                d[x] = d.get(x, 0) + 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.pairSums([5,6,5], 11)
    a.pairSums([5,6,5,6], 11)
    a.pairSums([5, 6, 3, -6, 2, 1, 1, 0, 8, 0], 2)