# -*- coding: utf-8 -*-
# ======================================
# @File    : 1627.py
# @Time    : 2020/10/23 1:31 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1627. 带阈值的图连通性](https://leetcode-cn.com/problems/graph-connectivity-with-threshold/)
    """
    @timeit
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        def primes(x):
            res = set()
            for i in range(threshold+1, int((x**0.5)+1)+1):
                if x % i == 0:
                    res.add(i)
                    if x//i > threshold:
                        res.add(x//i)
            return res
        pr = [set() for _ in range(n+1)]
        for i in range(1, n+1):
            for j in primes(i):
                pr[j].add(i)
        uf = [i for i in range(n+1)]
        def find(u):
            if uf[u] == u: return u
            else:
                uf[u] = find(uf[u])
                return uf[u]
        def union(u, v):
            x, y = find(u), find(v)
            if x == y: return
            uf[x] = y
            find(u)
        for i in range(1, n+1):
            pri = list(pr[i])
            m = len(pri)
            for j in range(m):
                for k in range(i+1, m):
                    union(pri[j], pri[k])
        print(pr)
        return [find(u) == find(v) for u, v in queries]

if __name__ == '__main__':
    a = Solution()
    a.areConnected(n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]])
    a.areConnected(n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]])
    a.areConnected(n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]])