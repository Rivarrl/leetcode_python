# -*- coding: utf-8 -*-
# ======================================
# @File    : 5377.py
# @Time    : 2020/4/5 10:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5377. 将二进制表示减到 1 的步骤数](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)
    """
    @timeit
    def numSteps(self, s: str) -> int:
        n = i = 0
        for c in s[::-1]:
            if c == '1':
                n += (1 << i)
            i += 1
        res = 0
        while n > 1:
            if n & 1:
                n += 1
            else:
                n //= 2
            res += 1
        return res

    @timeit
    def numSteps2(self, s: str) -> int:
        i = len(s) - 1
        s = [e for e in s]
        res = 0
        while i > 0:
            if s[i] == '0':
                res += 1
                i -= 1
            else:
                res += 1
                while i >= 0 and s[i] == '1':
                    res += 1
                    i -= 1
                if i > 0: s[i] = '1'
        return res

if __name__ == '__main__':
    a = Solution()
    a.numSteps(s = "1101")
    a.numSteps(s = "10")
    a.numSteps(s = "1")