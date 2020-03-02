# -*- coding: utf-8 -*-
# ======================================
# @File    : 953.py
# @Time    : 2020/3/2 14:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = 0
        for word in words:
            m = max(m, len(word))
        d = {order[i]: i for i in range(26)}
        def compare(i, words):
            if i == m: return True
            x = []
            l = '@'
            rec: List[List[str]] = [[]]
            for word in words:
                if i == len(word):
                    x.append(-1)
                    continue
                c = word[i]
                if c != l:
                    l = c
                    rec.append([word])
                else:
                    rec[-1].append(word)
                x.append(d[c])
            if x != sorted(x): return False
            for r in rec:
                if not compare(i+1, r): return False
            return True
        return compare(0, words)


if __name__ == '__main__':
    a = Solution()
    a.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
    a.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")
    a.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")