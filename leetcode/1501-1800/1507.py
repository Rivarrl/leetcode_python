# -*- coding: utf-8 -*-
# ======================================
# @File    : 1507
# @Time    : 2021/2/24 13:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1507. 转变日期格式](https://leetcode-cn.com/problems/reformat-date/)
    """
    @timeit
    def reformatDate(self, date: str) -> str:
        month_arr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day, month, year = date.split(' ')
        day = day[:-2]
        month = str(month_arr.index(month) + 1)
        day = '0' + day if len(day) == 1 else day
        month = '0' + month if len(month) == 1 else month
        return '{}-{}-{}'.format(year, month, day)

if __name__ == '__main__':
    a = Solution()
    a.reformatDate(date = "20th Oct 2052")
    a.reformatDate(date = "6th Jun 1933")
    a.reformatDate(date = "26th May 1960")