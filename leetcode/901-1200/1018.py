# -*- coding: utf-8 -*-
# ======================================
# @File    : 1018.py
# @Time    : 2020/5/9 0:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1018. 可被 5 整除的二进制前缀](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/submissions/)
    """
    @timeit
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        c = 0
        for x in A:
            c = ((c << 1) | x) % 5
            res.append(c==0)
        return res

if __name__ == '__main__':
    a = Solution()
    a.prefixesDivBy5([0,1,1])
    a.prefixesDivBy5([1,1,1])
    a.prefixesDivBy5([0,1,1,1,1,1])
    a.prefixesDivBy5([1,1,1,0,1])