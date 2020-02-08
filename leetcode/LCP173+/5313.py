# -*- coding: utf-8 -*-
# ======================================
# @File    : 5313.py
# @Time    : 2/8/20 10:40 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5313. 时钟指针的夹角]()
    """
    @timeit
    def angleClock(self, hour: int, minutes: int) -> float:
        h_tic = (hour % 12) + minutes / 60
        m_tic = minutes
        r = abs(h_tic / 12 * 360 - m_tic / 60 * 360)
        return r if r < 180 else 360 - r

if __name__ == '__main__':
    a = Solution()
    a.angleClock(hour = 12, minutes = 30)
    a.angleClock(3,30)
    a.angleClock(3,15)
    a.angleClock(4,50)
    a.angleClock(12,0)
    a.angleClock(1,57)