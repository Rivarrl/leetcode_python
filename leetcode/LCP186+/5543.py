# -*- coding: utf-8 -*-
# ======================================
# @File    : 5543.py
# @Time    : 2020/10/18 10:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5543. 两个相同字符之间的最长子字符串]()
    """
    @timeit
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        res = -1
        for k, ids in d.items():
            if len(ids) > 1:
                res = max(res, ids[-1] - ids[0] - 1)
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxLengthBetweenEqualCharacters(s = "aa")
    a.maxLengthBetweenEqualCharacters(s = "abca")
    a.maxLengthBetweenEqualCharacters(s = "cbzxy")
    a.maxLengthBetweenEqualCharacters(s = "cabbac")