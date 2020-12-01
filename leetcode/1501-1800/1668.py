# -*- coding: utf-8 -*-
# ======================================
# @File    : 1668.py
# @Time    : 2020/12/2 0:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1668. 最大重复子字符串]()
    """
    @timeit
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        res = 0
        for i in range(1, n // m + 1):
            if word * i in sequence:
                res = i
        return res


if __name__ == '__main__':
    a = Solution()
    a.maxRepeating(sequence = "ababc", word = "ab")
    a.maxRepeating(sequence = "ababc", word = "ba")
    a.maxRepeating(sequence = "ababc", word = "ac")