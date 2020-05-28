# -*- coding: utf-8 -*-
# ======================================
# @File    : 1450.py
# @Time    : 2020/5/26 19:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1450. 在既定时间做作业的学生人数]()
    """
    @timeit
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for st, ed in zip(startTime, endTime):
            if st <= queryTime <= ed:
                res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4)
    a.busyStudent(startTime = [4], endTime = [4], queryTime = 4)
    a.busyStudent(startTime = [4], endTime = [4], queryTime = 5)
    a.busyStudent(startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7)
    a.busyStudent(startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5)