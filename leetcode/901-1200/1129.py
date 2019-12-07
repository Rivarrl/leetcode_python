# -*- coding: utf-8 -*-
# ======================================
# @File    : 1129.py
# @Time    : 2019/12/7 17:14
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1129. 颜色交替的最短路径](https://leetcode-cn.com/problems/shortest-path-with-alternating-colors/)
    """
    @timeit
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        """
        思路：bfs
        """
        res = [-1] * n
        graph = [list() for _ in range(n)]
        for e in red_edges: graph[e[0]].append((e[1], 0))
        for e in blue_edges: graph[e[0]].append((e[1], 1))
        stk = [(0, 0, 0), (0, 1, 0)]
        vis = {(0, 0), (0, 1)}
        while stk:
            u, u_color, step = stk.pop()
            if res[u] == -1: res[u] = step
            for v, v_color in graph[u]:
                if v_color != u_color and not (v, v_color) in vis:
                    vis.add((v, v_color))
                    stk.insert(0, (v, v_color, step+1))
        return res


if __name__ == '__main__':
    a = Solution()
    a.shortestAlternatingPaths(3, [[0,1],[1,2]], [])
    a.shortestAlternatingPaths(3, [[0,1]], [[2,1]])
    a.shortestAlternatingPaths(3, [[1,0]], [[2,1]])
    a.shortestAlternatingPaths(3, [[0,1]], [[1,2]])
    a.shortestAlternatingPaths(3, [[0,1],[0,2]], [[1,0]])
    a.shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]])
