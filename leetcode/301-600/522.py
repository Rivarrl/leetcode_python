# -*- coding: utf-8 -*-
# ======================================
# @File    : 522.py
# @Time    : 2020/5/9 18:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [522. 最长特殊序列 II](https://leetcode-cn.com/problems/longest-uncommon-subsequence-ii/)
    """
    @timeit
    def findLUSlength(self, strs: List[str]) -> int:
        d = {}
        for s in strs: d[s] = d.get(s, 0) + 1
        ss = sorted(list(set(strs)), key=lambda x:(-len(x), x))
        res = -1
        n = len(ss)
        def ok(x, y):
            i = j = 0
            n, m = len(x), len(y)
            while i < n and j < m:
                if x[i] == y[j]: j += 1
                i += 1
            return j == m
        for i in range(n):
            if d[ss[i]] > 1: continue
            for j in range(i):
                if ok(ss[j], ss[i]): break
            else:
                res = len(ss[i])
                break
        return res

if __name__ == '__main__':
    a = Solution()
    a.findLUSlength(["aba", "cdc", "eae", "dddd"])
    a.findLUSlength(["aaa", "aaa", "aa"])
    a.findLUSlength(["aabbcc", "aabbcc","c"])
    a.findLUSlength(["aabbcc", "aabbcc","cb","abc"])
    a.findLUSlength(["abcabc","abcabc","abcabc","abc","abc","bac"])