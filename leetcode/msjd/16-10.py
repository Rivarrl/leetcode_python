# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-10.py
# @Time    : 2020/11/11 1:16 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.10. 生存人数](https://leetcode-cn.com/problems/living-people-lcci/)
    """
    @timeit
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        l, r = min(birth), max(death) + 1
        n = r - l + 1
        a = [0] * n
        for i, j in zip(birth, death):
            a[j - l + 1] -= 1
            a[i - l] += 1
        res = m = c = 0
        for i, x in enumerate(a):
            c += x
            if c > m:
                res = i + l
                m = c
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxAliveYear([1900, 1901, 1950], [1948, 1951, 2000])