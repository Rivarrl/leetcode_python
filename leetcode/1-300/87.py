# -*- coding: utf-8 -*-
# ======================================
# @File    : 87.py
# @Time    : 2019/11/25 10:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from functools import lru_cache
class Solution:
    """
    [87. 扰乱字符串](https://leetcode-cn.com/problems/scramble-string/)
    """
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        思路：分治法
        """
        if s1 == s2: return True
        if sorted(s1) != sorted(s2): return False
        n = len(s1)
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False


if __name__ == '__main__':
    a = Solution()
    a.isScramble("great", "rgeat")