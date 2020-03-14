# -*- coding: utf-8 -*-
# ======================================
# @File    : t2.py
# @Time    : 2020/3/14 19:38
# @Author  : Rivarrl
# ======================================
import sys

# t2 手里的钱能发牛牛几个月的工资 60%
# 输入：n 面额种类, m 需要发牛牛的最低工资，n行面额和数量
# 输出：最多能发的工资月数，不设找零
"""
输入：
3 51
100 1
50 4
1 2
输出：
4
"""

def solve():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    d = {}
    arr = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        d[x] = y
        arr.append(x)
    arr.sort()
    ans = 0
    for e in arr[::-1]:
        if e >= m:
            ans += d[e]
            d[e] = 0
        else: break
    # 每次挑选满足条件的最小值，没有满足条件的就挑最大的
    def dfs(p):
        nonlocal ans
        for e in arr:
            if e >= p and d[e] > 0:
                d[e] -= 1
                ans += 1
                return True
        for e in arr[::-1]:
            if d[e] > 0:
                d[e] -= 1
                p -= e
                break
        else:
            return False
        return dfs(p)

    while dfs(m):
        continue
    return ans

if __name__ == '__main__':
    res = solve()
    print(res)