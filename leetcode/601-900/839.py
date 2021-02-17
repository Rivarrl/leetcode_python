# -*- coding: utf-8 -*-
# ======================================
# @File    : 839.py
# @Time    : 2021/1/31 19:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [839. 相似字符串组](https://leetcode-cn.com/problems/similar-string-groups/)
    """
    @timeit
    def numSimilarGroups(self, strs: List[str]) -> int:
        def f(s, t):
            tot = 0
            for i, (c1, c2) in enumerate(zip(s, t)):
                if c1 != c2:
                    tot += 1
                    if tot > 2: return False
            return True
        def find(u):
            if dsu[u] != u:
                dsu[u] = find(dsu[u])
            return dsu[u]
        def union(u, v):
            x, y = find(u), find(v)
            if x == y: return
            dsu[x] = y
        n = len(strs)
        dsu = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if f(strs[i], strs[j]):
                    union(i, j)
        res = 0
        for i in range(n):
            if dsu[i] == i:
                res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.numSimilarGroups(strs = ["tars","rats","arts","star"])
    a.numSimilarGroups(strs = ["omv","ovm"])