# -*- coding: utf-8 -*-
# ======================================
# @File    : 387
# @Time    : 2020/1/11 18:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [387. 字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)
    """
    @timeit
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            d[c] = d.get(c, []) + [i]
        for i, c in enumerate(s):
            if len(d[c]) == 1:
                return i
        return -1


    def firstUniqChar2(self, s: str) -> int:
        n = len(s)
        m = n
        for i in range(26):
            x = chr(ord('a') + i)
            if s.find(x) >= 0 and s.find(x) == s.rfind(x):
                j = s.index(x)
                if j < m: m = j
        return -1 if m == n else m

if __name__ == '__main__':
    a = Solution()
    a.firstUniqChar("leetcode")
    a.firstUniqChar("loveleetcode")