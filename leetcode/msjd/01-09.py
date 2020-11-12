# -*- coding: utf-8 -*-
# ======================================
# @File    : 01-09.py
# @Time    : 2020/11/13 0:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 01.09. 字符串轮转](https://leetcode-cn.com/problems/string-rotation-lcci/)
    """
    @timeit
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s1 in s2 * 2


if __name__ == '__main__':
    a = Solution()
    a.isFlipedString(s1 = "waterbottle", s2 = "erbottlewat")
    a.isFlipedString(s1 = "aa", s2 = "aba")