# -*- coding: utf-8 -*-
# ======================================
# @File    : 1002.py
# @Time    : 2019/11/26 10:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1002. 查找常用字符](https://leetcode-cn.com/problems/find-common-characters/comments/)
    """
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        d = Counter(A[0])
        for a in A[1:]:
            d1 = Counter(a)
            for i in range(26):
                x = chr(ord('a') + i)
                d[x] = min(d.get(x, 0), d1.get(x, 0))
        res = []
        for k, v in d.items():
            if v == 0: continue
            for i in range(v):
                res.append(k)
        return res