# -*- coding: utf-8 -*-
# ======================================
# @File    : 1647.py
# @Time    : 2020/11/10 1:13 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1647. 字符频次唯一的最小删除次数]()
    """
    @timeit
    def minDeletions(self, s: str) -> int:
        from collections import Counter
        ctr = Counter(s)
        vals = Counter(ctr.values())
        sv = sorted(vals.keys())
        res = 0
        last = [0]
        for i in range(len(sv)):
            if vals[sv[i]] > 1:
                res += (sv[i] - last[-1]) * (vals[sv[i]] - 1)
            last.append(sv[i])
        print(vals)
        return res


if __name__ == '__main__':
    a = Solution()
    a.minDeletions(s = "aab")
    a.minDeletions(s = "aaabbbcc")
    a.minDeletions(s = "ceabaacb")