# -*- coding: utf-8 -*-
# ======================================
# @File    : 5465.py
# @Time    : 2020/7/19 10:45
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5465. 子树中标签相同的节点数]()
    """
    @timeit
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = [list() for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        res = [0] * n
        vis = [False] * n
        def dfs(u):
            nonlocal res
            vis[u] = True
            alp = [0] * 26
            j = ord(labels[u]) - ord('a')
            alp[j] = 1
            for v in g[u]:
                if vis[v]: continue
                tmp = dfs(v)
                for i in range(26):
                    alp[i] += tmp[i]
            res[u] = alp[j]
            return alp
        dfs(0)
        return res

if __name__ == '__main__':
    a = Solution()
    # a.countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd")
    # a.countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb")
    # a.countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab")
    # a.countSubTrees(n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa")
    # a.countSubTrees(n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa")
    a.countSubTrees(4,[[0,2],[0,3],[1,2]],"aeed")