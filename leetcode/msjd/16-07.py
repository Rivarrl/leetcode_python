# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-07.py
# @Time    : 2020/8/13 23:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.07. 最大数值](https://leetcode-cn.com/problems/maximum-lcci/)
    """
    @timeit
    def maximum(self, a: int, b: int) -> int:
        return (abs(a-b) + a + b) // 2

if __name__ == '__main__':
    a = Solution()
    a.maximum(1,2)