# -*- coding: utf-8 -*-
# ======================================
# @File    : 5323.py
# @Time    : 2020/2/23 12:29
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5323. 根据数字二进制下 1 的数目排序](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/)
    """
    def sortByBits(self, arr: List[int]) -> List[int]:
        from functools import cmp_to_key
        def my_cmp(x, y):
            sx, sy = bin(x), bin(y)
            cx, cy = sx.count('1'), sy.count('1')
            if cx == cy:
                return 1 if x > y else -1
            else:
                return 1 if cx > cy else -1
        arr.sort(key=cmp_to_key(my_cmp))
        return arr
