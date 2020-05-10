# -*- coding: utf-8 -*-
# ======================================
# @File    : 5406.py
# @Time    : 2020/5/10 10:43
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5406. 收集树上所有苹果的最少时间](https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree/)
    """
    @timeit
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        from collections import defaultdict
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
        def dfs(u):
            res = 0
            for v in g[u]:
                ch = dfs(v)
                res += ch
                if hasApple[v] or ch > 0:
                    res += 1
            return res
        return dfs(0) * 2

if __name__ == '__main__':
    a = Solution()
    true, false = True, False
    a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false])
    a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false])
    a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false])
    a.minTime(4, [[0,1],[1,2],[0,3]], [true,true,true,true])