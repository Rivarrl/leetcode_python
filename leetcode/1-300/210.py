# -*- coding: utf-8 -*-
# ======================================
# @File    : 210.py
# @Time    : 2019/11/12 10:23
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [210. 课程表 II](https://leetcode-cn.com/problems/course-schedule-ii/)
    """
    @timeit
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        思路：拓扑排序，从入度为0的点开始，bfs找环
        """
        # 构图
        graph = [set() for _ in range(numCourses)]
        degree_in = [0] * numCourses
        for a, b in prerequisites:
            graph[b].add(a)
            degree_in[a] += 1
        stk = [i for i in range(numCourses) if degree_in[i] == 0]
        res = []
        while stk:
            v = stk.pop()
            res.append(v)
            for u in graph[v]:
                degree_in[u] -= 1
                if degree_in[u] == 0:
                    stk.append(u)
        if len(res) != numCourses: return []
        return res

if __name__ == '__main__':
    a = Solution()
    a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    a.findOrder(8, [[1,0],[2,0],[3,1],[3,2],[5,4],[6,4],[7,6],[7,5]])
    a.findOrder(4, [[1,0],[2,1],[0,2],[3,2]])