# -*- coding: utf-8 -*-
# ======================================
# @File    : 290.py
# @Time    : 2020/12/16 10:01 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [290. 单词规律](https://leetcode-cn.com/problems/word-pattern/)
    """
    @timeit
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern and not s: return True
        d = {}
        dr = {}
        arr = s.split(' ')
        if len(arr) != len(pattern): return False
        n = len(arr)
        for i in range(n):
            if d.get(pattern[i], arr[i]) != arr[i]:
                return False
            if dr.get(arr[i], pattern[i]) != pattern[i]:
                return False
            d[pattern[i]] = arr[i]
            dr[arr[i]] = pattern[i]
        return True

if __name__ == '__main__':
    a = Solution()
    a.wordPattern(pattern = "abba", s = "dog cat cat dog")
    a.wordPattern(pattern = "abba", s = "dog cat cat fish")
    a.wordPattern(pattern = "aaaa", s = "dog cat cat dog")
    a.wordPattern(pattern = "abba", s = "dog dog dog dog")