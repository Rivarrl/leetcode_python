# -*- coding: utf-8 -*-
# ======================================
# @File    : 5432.py
# @Time    : 2020/6/27 22:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5432. 去掉最低工资和最高工资后的工资平均值](https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary)
    """
    @timeit
    def average(self, salary: List[int]) -> float:
        mi, ma = 0x3f3f3f3f, 0
        tot = 0
        n = len(salary)
        for i in range(n):
            mi = min(mi, salary[i])
            ma = max(ma, salary[i])
            tot += salary[i]
        return (tot - mi - ma) / (len(salary) - 2)


if __name__ == '__main__':
    a = Solution()
    a.average([4000,3000,1000,2000])
    a.average([1000,2000,3000])
    a.average([6000,5000,4000,3000,2000,1000])
    a.average([8000,9000,2000,3000,6000,1000])