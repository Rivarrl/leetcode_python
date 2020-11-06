# -*- coding: utf-8 -*-
# ======================================
# @File    : 1638.py
# @Time    : 2020/11/6 12:59 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1638. 统计只差一个字符的子串数目]()
    """
    @timeit
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        res = 0
        dp = {}
        for k in range(min(n, m)):
            tmp = {}
            for i in range(k, n):
                for j in range(k, m):
                    x = 1 if s[i] != t[j] else 0
                    cur = dp.get((i-k,j-k), 0) + x
                    if cur == 1:
                        res += 1
                    tmp[(i-k, j-k)] = cur
            dp = tmp.copy()
        return res


if __name__ == '__main__':
    a = Solution()
    a.countSubstrings(s = "aba", t = "baba")
    a.countSubstrings(s = "ab", t = "bb")
    a.countSubstrings(s = "a", t = "a")
    a.countSubstrings(s = "abe", t = "bbc")