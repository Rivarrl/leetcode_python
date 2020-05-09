# -*- coding: utf-8 -*-
# ======================================
# @File    : 01-01.py
# @Time    : 2020/5/9 23:03
# @Author  : Rivarrl
# ======================================
# [面试题 01.01. 判定字符是否唯一](https://leetcode-cn.com/problems/is-unique-lcci/)
from algorithm_utils import *

class Solution:
    @timeit
    def isUnique(self, astr: str) -> bool:
        d = set()
        for s in astr:
            if s in d:
                return False
            d.add(s)
        return True

if __name__ == '__main__':
    a = Solution()
    a.isUnique("leetcode")
    a.isUnique("abc")