# -*- coding: utf-8 -*-
# ======================================
# @File    : 50.py
# @Time    : 2020/3/12 23:51
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
# [面试题50. 第一个只出现一次的字符](https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/)
class Solution:
    @timeit
    def firstUniqChar(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for k, v in d.items():
            if v == 1:
                return k
        return " "

if __name__ == '__main__':
    a = Solution()
    a.firstUniqChar(s = "abaccdeff")