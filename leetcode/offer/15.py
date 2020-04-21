# -*- coding: utf-8 -*-
# ======================================
# @File    : 15.py
# @Time    : 2020/4/21 15:44
# @Author  : Rivarrl
# ======================================
# [面试题15. 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n = n & (n-1)
        return res


if __name__ == '__main__':
    a = Solution()
    a.hammingWeight(13)
