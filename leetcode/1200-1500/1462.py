# -*- coding: utf-8 -*-
# ======================================
# @File    : 1462.py
# @Time    : 2020/6/1 20:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1462. 课程安排 IV](https://leetcode-cn.com/problems/course-schedule-iv/)
    """
    @timeit
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        inf = 0x3f3f3f3f
        f = [[inf] * n for _ in range(n)]
        for u, v in prerequisites:
            f[u][v] = 1
        for i in range(n):
            f[i][i] = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    f[j][k] = min(f[j][k], f[j][i] + f[i][k])
        res = []
        for u, v in queries:
            res.append(f[u][v] != inf)
        return res

if __name__ == '__main__':
    a = Solution()
    # a.checkIfPrerequisite(n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]])
    # a.checkIfPrerequisite(n = 2, prerequisites = [], queries = [[1,0],[0,1]])
    # a.checkIfPrerequisite(n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])
    # a.checkIfPrerequisite(n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]])
    # a.checkIfPrerequisite(n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]])
    a.checkIfPrerequisite(13, [[2,1],[2,7],[2,0],[2,10],[2,11],[1,7],[1,0],[1,9],[1,4],[1,11],[7,3],[7,9],[7,4],[7,11],[7,8],[3,6],[3,12],[3,5],[6,10],[6,8],[0,4],[12,9],[12,8],[9,4],[9,11],[9,8],[9,5],[10,8],[4,8]],
                          [[12,11],[11,1],[10,12],[9,10],[10,11],[11,12],[2,7],[6,8],[3,2],[9,5],[8,7],[1,4],[3,12],[9,6],[4,3],[11,4],[5,7],[3,9],[3,1],[8,12],[5,12],[0,8],[10,5],[10,11],[12,11],[12,9],[5,4],[11,5],[12,10],[11,0],[6,10],[11,7],[8,10],[2,1],[3,4],[8,7],[11,6],[9,11],[1,4],[10,8],[7,1],[8,7],[9,7],[5,1],[8,10],[11,8],[8,12],[9,12],[12,11],[6,12],[12,11],[6,10],[9,12],[8,10],[8,11],[8,5],[7,9],[12,11],[11,12],[8,0],[12,11],[7,0],[8,7],[5,11],[11,8],[1,9],[4,10],[11,6],[10,12]])

