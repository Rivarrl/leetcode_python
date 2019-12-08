# -*- coding: utf-8 -*-
# ======================================
# @File    : 5279.py
# @Time    : 2019/12/8 10:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5279. 整数的各位积和之差
    """
    @timeit
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce
        arr = list(map(int, [e for e in str(n)]))
        return reduce(lambda x, y: x * y, arr) - sum(arr)

if __name__ == '__main__':
    a = Solution()
    a.subtractProductAndSum(234)