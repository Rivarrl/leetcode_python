# -*- coding: utf-8 -*-
# ======================================
# @File    : 1486.py
# @Time    : 2020/6/28 12:55 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1486. 数组异或操作](https://leetcode-cn.com/problems/xor-operation-in-an-array/)
    """
    @timeit
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(start, start + 2 * n, 2):
            res ^= i
        return res


if __name__ == '__main__':
    a = Solution()
    a.xorOperation(5, 0)
    a.xorOperation(4, 3)
    a.xorOperation(1, 7)
    a.xorOperation(10, 5)