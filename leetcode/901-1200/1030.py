# -*- coding: utf-8 -*-
# ======================================
# @File    : 1030.py
# @Time    : 2019/12/27 23:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1030. 距离顺序排列矩阵单元格](https://leetcode-cn.com/problems/matrix-cells-in-distance-order/)
    """
    @timeit
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # 自定义排序,有点慢
        from functools import cmp_to_key
        return sorted([[i, j] for i in range(R) for j in range(C)], key=cmp_to_key(lambda x, y: abs(x[0] - r0) + abs(x[1] - c0) - abs(y[0] - r0) - abs(y[1] - c0)))


    @timeit
    def allCellsDistOrder2(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # 广度优先搜索
        stk = [[r0, c0]]
        res = []
        vis = [[0] * C for _ in range(R)]
        vis[r0][c0] = 1
        dxy = [[0,1],[1,0],[-1,0],[0,-1]]
        while stk:
            x, y = stk.pop()
            res.append([x, y])
            for dx, dy in dxy:
                i, j = x + dx, y + dy
                if 0 <= i < R and 0 <= j < C and not vis[i][j]:
                    vis[i][j] = 1
                    stk.insert(0, [i, j])
        return res


if __name__ == '__main__':
    a = Solution()
    a.allCellsDistOrder(R = 1, C = 2, r0 = 0, c0 = 0)
    a.allCellsDistOrder(R = 2, C = 2, r0 = 0, c0 = 1)
    a.allCellsDistOrder(R = 2, C = 3, r0 = 1, c0 = 2)
    a.allCellsDistOrder2(R = 1, C = 2, r0 = 0, c0 = 0)
    a.allCellsDistOrder2(R = 2, C = 2, r0 = 0, c0 = 1)
    a.allCellsDistOrder2(R = 2, C = 3, r0 = 1, c0 = 2)
