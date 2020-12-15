# -*- coding: utf-8 -*-
# ======================================
# @File    : 05-08.py
# @Time    : 2020/12/15 10:03 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 05.08. 绘制直线](https://leetcode-cn.com/problems/draw-line-lcci/)
    """
    @timeit
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        res = [0] * length
        st = y * w
        l, r = x1 + st, x2 + st
        fr, to = l // 32, r // 32
        if fr == to:
            res[fr] = ((1 << (x2 + 1 - x1)) - 1) << (31 - (x2 % 32))
        else:
            for i in range(fr + 1, to):
                res[i] = -1
            res[fr] = (1 << (32 - (x1 % 32))) - 1
            res[to] = ((1 << (x2 % 32 + 1)) - 1) << (31 - (x2 % 32))
        mask = 0xffffffff
        if res[fr] > 0x7fffffff:
            res[fr] = - ((mask ^ res[fr]) + 1)
        if res[to] > 0x7fffffff:
            res[to] = - ((mask ^ res[to]) + 1)
        return res

if __name__ == '__main__':
    a = Solution()
    a.drawLine(length = 1, w = 32, x1 = 0, x2 = 2, y = 0)
    a.drawLine(length = 1, w = 32, x1 = 30, x2 = 31, y = 0)
    a.drawLine(length = 3, w = 96, x1 = 0, x2 = 95, y = 0)
    a.drawLine(15, 96, 81, 95, 1)