# -*- coding: utf-8 -*-
# ======================================
# @File    : 5311.py
# @Time    : 2/8/20 10:32 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [5311. 将数字变成 0 的操作次数](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero/)
    """
    @timeit
    def numberOfSteps(self, num: int) -> int:
        ctr = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            ctr += 1
        return ctr


if __name__ == '__main__':
    a = Solution()
    a.numberOfSteps(14)
    a.numberOfSteps(8)
    a.numberOfSteps(123)
    a.numberOfSteps(9999999)
