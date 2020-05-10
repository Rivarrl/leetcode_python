# -*- coding: utf-8 -*-
# ======================================
# @File    : 5407.py
# @Time    : 2020/5/10 11:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5407. 切披萨的方案数](https://leetcode-cn.com/problems/number-of-ways-of-cutting-a-pizza/)
    """
    @timeit
    def ways(self, pizza: List[str], k: int) -> int:
        from functools import lru_cache
        mod = 10 ** 9 + 7
        n = len(pizza)
        m = len(pizza[0])
        @lru_cache(None)
        def dfs(x, y, z):
            if z == 0:
                for i in range(x, n):
                    for j in range(y, m):
                        if pizza[i][j] == 'A': return 1
                return 0
            res = 0
            for i in range(x, n-1):
                for j in range(y, m):
                    if pizza[i][j] == 'A':
                        res += dfs(i+1, j, z-1)
                        break
            for j in range(y, m-1):
                for i in range(x, n):
                    if pizza[i][j] == 'A':
                        res += dfs(i, j+1, z-1)
                        break
            return res
        return dfs(0, 0, k-1)

if __name__ == '__main__':
    a = Solution()
    # a.ways(pizza = ["A..","AAA","..."], k = 3)
    # a.ways(pizza = ["A..","AA.","..."], k = 3)
    # a.ways(pizza = ["A..","A..","..."], k = 1)
    # a.ways([".A","AA","A."], 3)
    a.ways([".A..A","A.A..","A.AA.","AAAA.","A.AA."], 5)