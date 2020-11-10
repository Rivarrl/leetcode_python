# -*- coding: utf-8 -*-
# ======================================
# @File    : 1647.py
# @Time    : 2020/11/10 1:13 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1647. 字符频次唯一的最小删除次数](https://leetcode-cn.com/problems/minimum-deletions-to-make-character-frequencies-unique/)
    """
    @timeit
    def minDeletions(self, s: str) -> int:
        from collections import Counter
        ctr = Counter(s)
        vs = ctr.values()
        d = set()
        res = 0
        for v in vs:
            if v not in d:
                d.add(v)
            else:
                p = v
                while v > 0 and v in d:
                    v -= 1
                if v > 0:
                    d.add(v)
                res += p - v
        return res


if __name__ == '__main__':
    a = Solution()
    a.minDeletions(s = "aab")
    a.minDeletions(s = "aaabbbcc")
    a.minDeletions(s = "ceabaacb")