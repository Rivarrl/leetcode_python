# -*- coding: utf-8 -*-
# ======================================
# @File    : 886.py
# @Time    : 2020/6/4 18:38
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [886. 可能的二分法](https://leetcode-cn.com/problems/possible-bipartition/)
    """
    @timeit
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # dfs二分图染色
        g = [[True] * N for _ in range(N)]
        for u, v in dislikes:
            g[u-1][v-1] = g[v-1][u-1] = False
        group = [-1] * N
        def dfs(u, n=0):
            if group[u] != -1:
                return group[u] == n
            group[u] = n
            for v in range(N):
                if not g[u][v]:
                    if group[v] == n or (group[v] == -1 and not dfs(v, n ^ 1)):
                        return False
            return True
        for u in range(N):
            if group[u] == -1 and not dfs(u):
                return False
        return True

    @timeit
    def possibleBipartition2(self, N: int, dislikes: List[List[int]]) -> bool:
        # 并查集，将人分为a和b两组，然后将他们讨厌的人分为x(a讨厌的)和y(b讨厌的)两组
        # 所以a应与y连通，同理b与x连通
        arr = [0] * (N*2)
        for i in range(N*2):
            arr[i] = i
        def find(x):
            if arr[x] == x: return x
            arr[x] = find(arr[x])
            return arr[x]
        for u, v in dislikes:
            i, j = u-1, v-1
            a = find(i)
            b = find(j)
            x = find(i+N)
            y = find(j+N)
            if a == b: return False
            arr[x] = b
            arr[y] = a
        return True

if __name__ == '__main__':
    a = Solution()
    a.possibleBipartition2(N = 4, dislikes = [[1,2],[1,3],[2,4]])
    a.possibleBipartition2(N = 3, dislikes = [[1,2],[1,3],[2,3]])
    a.possibleBipartition2(N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]])