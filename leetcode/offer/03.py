# -*- coding: utf-8 -*-
# ======================================
# @File    : 03.py
# @Time    : 2020/4/21 12:31
# @Author  : Rivarrl
# ======================================
# [面试题03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = set()
        for e in nums:
            if e in d:
                return e
            d.add(e)


if __name__ == '__main__':
    a = Solution()
    a.findRepeatNumber([2,3,1,0,2,5,3])