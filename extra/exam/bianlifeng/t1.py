# -*- coding: utf-8 -*-
# ======================================
# @File    : t1.py
# @Time    : 2020/5/7 19:50
# @Author  : Rivarrl
# ======================================
def f(n, widths, values):
    m = len(widths)
    dp = [[0] * (n+1) for _ in range(m)]
    for i in range(m):
        for j in range(n+1):
            if j >= widths[i]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-widths[i]] + values[i])
    return max(dp[i][-1] for i in range(m))

from functools import lru_cache
def f2(n, widths, values):
    @lru_cache(None)
    def dfs(i, j):
        if i == m - 1: return 0 if widths[i] > j else values[i]
        res = dfs(i+1, j)
        if j >= widths[i]:
            res = max(res, dfs(i+1, j-widths[i]) + values[i])
        return res
    m = len(widths)
    return dfs(0, n)

n = int(input().strip())
line1 = input().strip()
line2 = input().strip()
widths = list(map(int, line1.split(',')))
values = list(map(int, line2.split(',')))
x = f2(n, widths, values)
print(x)