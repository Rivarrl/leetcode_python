# -*- coding: utf-8 -*-
# ======================================
# @File    : 525.py
# @Time    : 2020/5/9 17:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [525. 连续数组](https://leetcode-cn.com/problems/contiguous-array/)
    """
    @timeit
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}
        res = c = 0
        for i, x in enumerate(nums):
            c += x if x else -1
            if not c in d: d[c] = i
            else: res = max(res, i - d[c])
        return res

if __name__ == '__main__':
    a = Solution()
    a.findMaxLength([0,1])
    a.findMaxLength([0,1,0])
    a.findMaxLength([0,0,1,0,0,0,1,1])