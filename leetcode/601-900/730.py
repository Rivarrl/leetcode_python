# -*- coding: utf-8 -*-
# ======================================
# @File    : 730.py
# @Time    : 2020/12/26 1:37 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [730. 统计不同回文子序列](https://leetcode-cn.com/problems/count-different-palindromic-subsequences/)
    """
    @timeit
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        for i in range(n):
            S[:i]

if __name__ == '__main__':
    a = Solution()
    a.countPalindromicSubsequences(S = 'bccb')
    a.countPalindromicSubsequences(S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba')