# -*- coding: utf-8 -*-
# ======================================
# @File    : 52.py
# @Time    : 2020/10/17 19:17
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def totalNQueens(self, n: int) -> int:
        col = [0] * n
        dia1 = [0] * n
        dia2 = [0] * n
        def f(i, s):

if __name__ == '__main__':
    a = Solution()
    a.totalNQueens(4)