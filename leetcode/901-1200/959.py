# -*- coding: utf-8 -*-
# ======================================
# @File    : 959.py
# @Time    : 2021/1/25 16:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [959. 由斜杠划分区域](https://leetcode-cn.com/problems/regions-cut-by-slashes/)
    """
    @timeit
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = {(i, j): (i, j) for j in range(n+1) for i in range(n+1)}
        # 连接墙壁
        for i in range(n+1):
            dsu[(i, 0)] = dsu[(0, i)] = dsu[(n, i)] = dsu[(i, n)] = (0, 0)
        def find(u):
            if u != dsu[u]:
                dsu[u] = find(dsu[u])
            return dsu[u]
        res = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    x, y = find((i+1, j)), find((i, j+1))
                    if x == y:
                        res += 1
                    else:
                        dsu[x] = y
                elif grid[i][j] == '\\':
                    x, y = find((i+1, j+1)), find((i, j))
                    if x == y:
                        res += 1
                    else:
                        dsu[x] = y
        return res


if __name__ == '__main__':
    a = Solution()
    a.regionsBySlashes([" /", "/ "])
    a.regionsBySlashes([" /", "  "])
    a.regionsBySlashes(["\\/", "/\\"])
    a.regionsBySlashes(["/\\", "\\/"])
    a.regionsBySlashes(["//", "/ "])