# -*- coding: utf-8 -*-
# ======================================
# @File    : 5621.py
# @Time    : 2020/12/26 22:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5621. 无法吃午餐的学生数量]()
    """
    @timeit
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(sandwiches)
        t = 1
        while t:
            i = 0
            t = 0
            while i < n:
                while i < n and students[i] != sandwiches[0]:
                    i += 1
                if i == n: break
                t += 1
                students.pop(i)
                sandwiches.pop(0)
                n -= 1
        return len(sandwiches)


if __name__ == '__main__':
    a = Solution()
    a.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1])
    a.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])