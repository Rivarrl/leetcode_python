# -*- coding: utf-8 -*-
# ======================================
# @File    : 1768
# @Time    : 2021/2/24 13:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1768. 交替合并字符串](https://leetcode-cn.com/problems/merge-strings-alternately/)
    """
    @timeit
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def f(word1, word2, x=0):
            n, m = len(word1), len(word2)
            if n > m: return f(word2, word1, 1)
            res = ''
            for i in range(n):
                cur = word1[i] + word2[i]
                if x == 1: cur = cur[::-1]
                res += cur
            res += word2[n:]
            return res
        return f(word1, word2)


if __name__ == '__main__':
    a = Solution()
    a.mergeAlternately(word1 = "abc", word2 = "pqr")
    a.mergeAlternately(word1 = "ab", word2 = "pqrs")
    a.mergeAlternately(word1 = "abcd", word2 = "pq")