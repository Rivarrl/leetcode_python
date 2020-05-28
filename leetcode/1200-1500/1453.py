# -*- coding: utf-8 -*-
# ======================================
# @File    : 1453.py
# @Time    : 2020/5/26 20:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1453. 圆形靶内的最大飞镖数量](https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/)
    """
    @timeit
    def numPoints(self, points: List[List[int]], r: int) -> int:
        dist = lambda a, b: ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
        f = lambda o: sum(dist(p, o) <= r for p in points)
        res = 1
        for p1 in points:
            for p2 in points:
                if 0 < dist(p1, p2) <= 2*r:
                    # 向量mi，从原点到p1和p2中点
                    mi = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
                    # 向量mo，p1->p2的一半
                    mo = [(p1[0] - p2[0]) / 2, (p1[1] - p2[1]) / 2]
                    # 向量p1->p2的垂线方向的等长向量
                    p = [p1[1]-p2[1], p2[0]-p1[0]]
                    # 垂线高度h
                    h = (r**2 - mo[0]**2 - mo[1]**2) ** 0.5
                    # 将垂线长度归一化，再乘相应长度
                    s = (p[0]**2 + p[1]**2) ** 0.5
                    x = h/s
                    # 求原点
                    o = [mi[0] + p[0]*x, mi[1] + p[1]*x]
                    res = max(res, f(o))
        return res

if __name__ == '__main__':
    a = Solution()
    a.numPoints(points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2)
    a.numPoints(points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5)
    a.numPoints(points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1)
    a.numPoints(points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2)
    a.numPoints([[4,5],[-4,1],[-3,2],[-4,0],[0,2]], 5)