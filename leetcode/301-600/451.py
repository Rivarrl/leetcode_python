# -*- coding: utf-8 -*-
# ======================================
# @File    : 451.py
# @Time    : 2020/7/30 11:49 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [451. 根据字符出现频率排序](https://leetcode-cn.com/problems/sort-characters-by-frequency/)
    """
    @timeit
    def frequencySort(self, s: str) -> str:
        from collections import Counter, defaultdict
        d = Counter(s)
        dr = defaultdict(list)
        for k, v in d.items():
            dr[v].append(k)
        res = ''
        for k in sorted(dr.keys(), reverse=True):
            for v in dr[k]:
                res += v * k
        return res

if __name__ == '__main__':
    a = Solution()
    a.frequencySort("tree")
    a.frequencySort("cccaaa")
    a.frequencySort("Aabb")