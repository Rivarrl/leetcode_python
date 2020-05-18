# -*- coding: utf-8 -*-
# ======================================
# @File    : 5396.py
# @Time    : 2020/5/16 22:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5396. 连续字符]()
    """
    @timeit
    def maxPower(self, s: str) -> int:
        cur, res = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                cur = 1
            res = max(res, cur)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxPower("leetcode")
    a.maxPower("abbcccddddeeeeedcba")
    a.maxPower("triplepillooooow")
    a.maxPower("hooraaaaaaaaaaay")
    a.maxPower("tourist")
    a.maxPower("aa")
    a.maxPower("j")