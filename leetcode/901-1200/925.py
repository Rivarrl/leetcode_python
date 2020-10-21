# -*- coding: utf-8 -*-
# ======================================
# @File    : 925.py
# @Time    : 2020/10/21 12:57 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [925. 长按键入](https://leetcode-cn.com/problems/long-pressed-name/)
    """
    @timeit
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        n = len(name)
        t = len(typed)
        while i < n and j < t:
            a, b = i, j
            while i < n - 1 and name[i] == name[i+1]:
                i += 1
            while j < t - 1 and typed[j] == typed[j+1]:
                j += 1
            if name[i] != typed[j] or i - a > j - b:
                return False
            if i == n - 1 and j == t - 1:
                return True
            i += 1
            j += 1
        return False

if __name__ == '__main__':
    a = Solution()
    a.isLongPressedName(name = "alex", typed = "aaleex")
    a.isLongPressedName(name = "saeed", typed = "ssaaedd")
    a.isLongPressedName(name = "leelee", typed = "lleeelee")
    a.isLongPressedName(name = "laiden", typed = "laiden")