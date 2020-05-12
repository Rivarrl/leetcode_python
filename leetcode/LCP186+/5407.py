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
            flag = False
            for i in range(x, n-1):
                if flag:
                    res += dfs(i+1, y, z-1)
                    continue
                for j in range(y, m):
                    if pizza[i][j] == 'A':
                        res += dfs(i+1, y, z-1)
                        flag = True
                        break
            flag = False
            for j in range(y, m-1):
                if flag:
                    res += dfs(x, j+1, z-1)
                    continue
                for i in range(x, n):
                    if pizza[i][j] == 'A':
                        res += dfs(x, j+1, z-1)
                        flag = True
                        break
            return res
        return dfs(0, 0, k-1) % mod


    @timeit
    def ways2(self, pizza: List[str], k: int) -> int:
        # dp[i][j][k]表示以i，j为左上角的一块披萨切k刀的方案数
        mod = 10 ** 9 + 7
        n, m, r = len(pizza), len(pizza[0]), k
        dp = [[[0] * r for _ in range(m)] for _ in range(n)]
        pre = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] = pre[i+1][j] + pre[i][j+1] - pre[i][j] + int(pizza[i][j] == 'A')
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                dp[i][j][0] = int(pre[-1][-1] + pre[i][j] - pre[i][-1] - pre[-1][j] > 0)
                for k in range(1, r):
                    for x in range(i, n-1):
                        apple_num = pre[x+1][-1] + pre[i][j] - pre[i][-1] - pre[x+1][j]
                        if apple_num > 0:
                            dp[i][j][k] += dp[x+1][j][k-1]
                    for y in range(j, m-1):
                        apple_num = pre[-1][y+1] + pre[i][j] - pre[i][y+1] - pre[-1][j]
                        if apple_num > 0:
                            dp[i][j][k] += dp[i][y+1][k-1]
        return dp[0][0][-1] % mod


if __name__ == '__main__':
    a = Solution()
    a.ways2(pizza = ["A..","AAA","..."], k = 3)
    a.ways2(pizza = ["A..","AA.","..."], k = 3)
    a.ways2(pizza = ["A..","A..","..."], k = 1)
    a.ways2([".A","AA","A."], 3)
    a.ways2([".A..A","A.A..","A.AA.","AAAA.","A.AA."], 5)