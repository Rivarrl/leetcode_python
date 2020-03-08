# -*- coding: utf-8 -*-
# ======================================
# @File    : 5352.py
# @Time    : 2020/3/8 10:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return 'a' * (n - 1) + 'b'
        return 'a' * n


if __name__ == '__main__':
    a = Solution()
    a.generateTheString(4)
    a.generateTheString(2)
    a.generateTheString(7)