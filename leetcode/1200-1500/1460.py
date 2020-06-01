# -*- coding: utf-8 -*-
# ======================================
# @File    : 1460.py
# @Time    : 2020/6/1 20:08
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1460. 通过翻转子数组使两个数组相等](https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/)
    """
    @timeit
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        from collections import Counter
        return Counter(target) == Counter(arr)

if __name__ == '__main__':
    a = Solution()
    a.canBeEqual(target = [1,2,3,4], arr = [2,4,1,3])
    a.canBeEqual(target = [7], arr = [7])
    a.canBeEqual(target = [1,12], arr = [12,1])
    a.canBeEqual(target = [3,7,9], arr = [3,7,11])
    a.canBeEqual(target = [1,1,1,1,1], arr = [1,1,1,1,1])