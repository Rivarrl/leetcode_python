# -*- coding: utf-8 -*-
# ======================================
# @File    : 990.py
# @Time    : 2019/12/27 11:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [990. 等式方程的可满足性](https://leetcode-cn.com/problems/satisfiability-of-equality-equations/)
    """
    @timeit
    def equationsPossible(self, equations: List[str]) -> bool:
        # union-find
        id = [i for i in range(26)]
        get_id = lambda c: ord(c) - ord('a')
        def find(x):
            if id[x] == x: return x
            id[x] = find(id[x])
            return id[x]

        def union(x, y):
            p, q = find(x), find(y)
            if p == q: return
            id[p] = q
        eqs = [eq for eq in equations if '==' in eq]
        neqs = [eq for eq in equations if '!=' in eq]
        for eq in eqs:
            union(get_id(eq[0]), get_id(eq[3]))
        for neq in neqs:
            x, y = get_id(neq[0]), get_id(neq[3])
            if find(x) == find(y): return False
        return True


if __name__ == '__main__':
    a = Solution()
    a.equationsPossible(["a==b","b!=a"])
    a.equationsPossible(["b==a","a==b"])
    a.equationsPossible(["a==b","b==c","a==c"])
    a.equationsPossible(["a==b","b!=c","c==a"])
    a.equationsPossible(["c==c","b==d","x!=z"])
    a.equationsPossible(["b==d","c==a","h==a","d==d","a==b","h!=k","i==h"])
    a.equationsPossible(["a!=a"])