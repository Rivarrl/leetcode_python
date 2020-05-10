# -*- coding: utf-8 -*-
# ======================================
# @File    : t2.py
# @Time    : 2020/5/10 20:13
# @Author  : Rivarrl
# ======================================

def f(r, g, b, n):
    dp = [[0] * 3 for _ in range(n+1)]
    for i in range(n):
        dp[i+1][0] = min(dp[i][1], dp[i][2]) + r[i]
        dp[i+1][1] = min(dp[i][0], dp[i][2]) + g[i]
        dp[i+1][2] = min(dp[i][0], dp[i][1]) + b[i]
    return min(dp[-1])

if __name__ == '__main__':
    n = int(input())
    r, g, b = [0] * n, [0] * n, [0] * n
    for i in range(n):
        r[i], g[i], b[i] = map(int, input().strip().split(' '))
    res = f(r, g, b, n)
    print(res)
"""
4
100 77 73
41 74 83
9 91 93
50 16 31
"""