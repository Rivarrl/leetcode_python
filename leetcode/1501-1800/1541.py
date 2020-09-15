# -*- coding: utf-8 -*-
# ======================================
# @File    : 1541.py
# @Time    : 2020/9/15 1:15 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1541. 平衡括号字符串的最少插入次数]()
    """
    @timeit
    def minInsertions(self, s: str) -> int:
        x = 0
        res = 0
        for c in s:
            if c == "(":
                if x < 0:
                    y = -x
                    res += (y//2) + (y%2) * 2
                    x = 0
                elif x & 1:
                    res += 1
                    x -= 1
                x += 2
            else:
                x -= 1
        if x < 0:
            y = -x
            res += (y//2) + (y%2) * 2
        elif x > 0:
            res += x
        return res

if __name__ == '__main__':
    a = Solution()
    a.minInsertions(s = "(()))")
    a.minInsertions(s = "())")
    a.minInsertions(s = "))())(")
    a.minInsertions(s = "((((((")
    a.minInsertions(s = ")))))))")