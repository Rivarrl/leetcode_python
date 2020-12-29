# -*- coding: utf-8 -*-
# ======================================
# @File    : 756.py
# @Time    : 2020/12/29 1:50 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [756. 金字塔转换矩阵](https://leetcode-cn.com/problems/pyramid-transition-matrix/)
    """
    @timeit
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict
        d = defaultdict(set)
        for x, y, z in allowed:
            d[x, y].add(z)
        def f(s):
            if len(s) == 1: return True
            return any(f(ns) for ns in next_s(s, []))
        def next_s(s, cur, i=0):
            if i == len(s) - 1:
                yield "".join(cur)
            else:
                x, y = s[i], s[i+1]
                for z in d[x, y]:
                    cur.append(z)
                    for res in next_s(s, cur, i+1):
                        yield res
                    cur.pop()
        return f(bottom)

if __name__ == '__main__':
    a = Solution()
    a.pyramidTransition(bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"])
    a.pyramidTransition(bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"])
    a.pyramidTransition("CCC", ["CBB","ACB","ABD","CDB","BDC","CBC","DBA","DBB","CAB","BCB","BCC","BAA","CCD","BDD","DDD","CCA","CAA","CCC","CCB"])
