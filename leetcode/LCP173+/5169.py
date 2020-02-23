# -*- coding: utf-8 -*-
# ======================================
# @File    : 5169.py
# @Time    : 2020/2/23 10:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5169. 日期之间隔几天](https://leetcode-cn.com/problems/number-of-days-between-two-dates/)
    """
    @timeit
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        m = {
            1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31
        }
        d1 = [int(e) for e in date1.split('-')]
        d2 = [int(e) for e in date2.split('-')]
        r1 = len([e for e in range(1971, d1[0]) if (e % 4 == 0 and e % 100 != 0) or e % 400 == 0])
        r2 = len([e for e in range(1971, d2[0]) if (e % 4 == 0 and e % 100 != 0) or e % 400 == 0])
        y1 = d1[0] * 365 + r1
        y2 = d2[0] * 365 + r2
        m1 = sum(m[i] for i in range(1, d1[1])) + int(d1[1] > 2 and ((d1[0] % 4 == 0 and d1[0] % 100 != 0) or d1[0] % 400 == 0))
        m2 = sum(m[i] for i in range(1, d2[1])) + int(d2[1] > 2 and ((d2[0] % 4 == 0 and d2[0] % 100 != 0) or d2[0] % 400 == 0))
        return abs((y1+m1+d1[2]) - (y2+m2+d2[2]))


if __name__ == '__main__':
    a = Solution()
    a.daysBetweenDates(date1="2019-06-29", date2 = "2019-06-30")
    a.daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31")
    a.daysBetweenDates("1971-06-29", "2010-09-23")
    a.daysBetweenDates("2100-09-22", "1991-03-12")