# -*- coding: utf-8 -*-
# ======================================
# @File    : 724.py
# @Time    : 2020/4/23 0:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0]
        for e in nums:
            pre += [pre[-1] + e]
        for i in range(1, len(pre)):
            if pre[i-1] == pre[-1] - pre[i]:
                return i - 1
        return -1

if __name__ == '__main__':
    a = Solution()
    a.pivotIndex([1,7,3,6,5,6])
    a.pivotIndex([1,2,3])
    a.pivotIndex([-1,-1,-1,-1,-1,0])
    a.pivotIndex([-1,-1,0,1,1,0])