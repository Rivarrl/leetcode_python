# -*- coding: utf-8 -*-
# ======================================
# @File    : 5528.py
# @Time    : 2020/10/17 22:48
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5528. 网络信号最好的坐标]()
    """
    @timeit
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        dis = lambda x, y: (x**2 + y**2) ** 0.5
        d = {}
        for x, y, q in towers:
            for i in range(-radius, radius+1):
                for j in range(-radius, radius+1):
                    dij = dis(i, j)
                    if dij <= radius:
                        cur = int(q / (1 + dij))
                        d[(x + i, y + j)] = d.get((x+i, y+j), 0) + cur
        m = max(d.values())
        rx, ry = 50, 50
        for (x, y), v in d.items():
            if v == m:
                if rx > x or (rx == x and ry > y):
                    rx, ry = x, y
        return [rx, ry]

if __name__ == '__main__':
    a = Solution()
    a.bestCoordinate(towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2)
    a.bestCoordinate(towers = [[23,11,21]], radius = 9)
    a.bestCoordinate(towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2)
    a.bestCoordinate(towers = [[2,1,9],[0,1,9]], radius = 2)
    a.bestCoordinate([[28,6,30],[23,16,0],[21,42,22],[50,33,34],[14,7,50],[40,31,4],[39,45,17],[46,21,12],[45,36,45],[35,43,43],[29,41,48],[22,27,5],[42,44,45],[10,49,50],[47,43,26],[40,36,25],[10,25,6],[27,30,30],[50,35,20],[11,0,44],[34,29,28]], 12)