# -*- coding: utf-8 -*-
# ======================================
# @File    : 5126.py
# @Time    : 2019/12/14 22:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5126. 有序数组中出现次数超过25%的元素](https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array/)
    """
    @timeit
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        n = len(arr)
        for k, v in Counter(arr).items():
            if v >= n // 4 + 1:
                return k

if __name__ == '__main__':
    a = Solution()
    a.findSpecialInteger([1,2,2,6,6,6,6,7,10])