# -*- coding: utf-8 -*-
# ======================================
# @File    : 05.py
# @Time    : 2020/4/21 13:10
# @Author  : Rivarrl
# ======================================
# [面试题05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)

from algorithm_utils import *

class Solution:
    @timeit
    def replaceSpace(self, s: str) -> str:
        return ''.join(['%20' if e == ' ' else e for e in s])


if __name__ == '__main__':
    a = Solution()
    a.replaceSpace("We are happy.")