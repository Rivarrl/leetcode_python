# -*- coding: utf-8 -*-
# ======================================
# @File    : 1202.py
# @Time    : 2021/1/11 12:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1202. 交换字符串中的元素](https://leetcode-cn.com/problems/smallest-string-with-swaps/)
    """
    @timeit
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 找连通分量，用union-find，相同连接中的位置的字符相对字典序最低
        from collections import defaultdict
        def find(p):
            while parent[p] != p:
                p = parent[p]
            return p

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j: return
            if sz[root_i] > sz[root_j]:
                parent[root_j] = root_i
                sz[root_i] += sz[root_j]
            else:
                parent[root_i] = root_j
                sz[root_j] += sz[root_i]

        n = len(s)
        parent = [i for i in range(n)]
        sz = [1 for _ in range(n)]
        for i, j in pairs:
            union(i, j)
        d = defaultdict(list)
        for i in range(n):
            d[find(i)].append(i)
        ls = [e for e in s]
        for v in d.values():
            tmp = sorted([ls[e] for e in v])
            for i in range(len(v)):
                ls[v[i]] = tmp[i]
        s = ''.join(ls)
        return s

if __name__ == '__main__':
    a = Solution()
    a.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]])
    a.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]])
    a.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]])