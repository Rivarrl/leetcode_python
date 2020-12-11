# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-05.py
# @Time    : 2020/12/11 12:44 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.05. 递归乘法](https://leetcode-cn.com/problems/recursive-mulitply-lcci/)
    """
    @timeit
    def multiply(self, A: int, B: int) -> int:
        # 快速乘
        res = 0
        while B:
            if B & 1:
                res += A
            A <<= 1
            B >>= 1
        return res

    @timeit
    def multiply2(self, A: int, B: int) -> int:
        # 改成递归？
        if B == 0:
            return 0
        if B & 1:
            return A + self.multiply2(A << 1, B >> 1)
        else:
            return self.multiply2(A << 1, B >> 1)

if __name__ == '__main__':
    a = Solution()
    a.multiply(A = 1, B = 10)
    a.multiply(A = 3, B = 4)