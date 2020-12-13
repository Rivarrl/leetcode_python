# -*- coding: utf-8 -*-
# ======================================
# @File    : 01-05.py
# @Time    : 2020/12/12 20:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 01.05. 一次编辑](https://leetcode-cn.com/problems/one-away-lcci/)
    """
    @timeit
    def oneEditAway(self, first: str, second: str) -> bool:
        n, m = len(first), len(second)
        if abs(n - m) > 1: return False
        i = j = 0
        cost = 0
        while i < n and j < m and cost <= 1:
            if first[i] != second[j]:
                cost += 1
                if i < n - 1 and first[i+1] == second[j]:
                    i += 1
                elif j < m - 1 and second[j+1] == first[i]:
                    j += 1
            i += 1
            j += 1
        cost += n - i + m - j
        return cost <= 1

if __name__ == '__main__':
    a = Solution()
    a.oneEditAway(first = "pale", second = "ple")
    a.oneEditAway(first = "pales", second = "pal")
    a.oneEditAway("ab", "bc")