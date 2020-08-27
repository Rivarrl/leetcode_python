# -*- coding: utf-8 -*-
# ======================================
# @File    : 657.py
# @Time    : 2020/8/28 0:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [657. 机器人能否返回原点](https://leetcode-cn.com/problems/robot-return-to-origin/)
    """
    @timeit
    def judgeCircle(self, moves: str) -> bool:
        st = 0
        d = {"U":1, "D":-1, "L":-1j, "R":1j}
        for c in moves:
            st += d[c]
        return st == 0

if __name__ == '__main__':
    a = Solution()
    a.judgeCircle("UD")
    a.judgeCircle("LL")