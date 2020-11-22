# -*- coding: utf-8 -*-
# ======================================
# @File    : 5605.py
# @Time    : 2020/11/22 10:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

if __name__ == '__main__':
    a = Solution()
    a.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"])
    a.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"])
    a.arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"])