# -*- coding: utf-8 -*-
# ======================================
# @File    : t3.py
# @Time    : 2020/3/12 22:54
# @Author  : Rivarrl
# ======================================
"""
3. 整除的数组
小美曾经有一个特殊的数组，这个数组的长度为n。但是她在打恐怖游戏的时候被吓得忘记了这个数组长什
么样了。不过她还记得这个数组满足一些条件。
首先这个数组的每个数的范围都在L和R之间。包括端点。
除此之外，这个数组满足数组中的所有元素的和是k的倍数。
但是这样的数组太多了，小美想知道有多少个这样的数组。你只需要告诉她在模1e9+7意义下的答案就行
了。
一行四个整数n,k,L,R
（1≤n≤1e5 1≤k≤10 1≤L≤R≤1e9）
输出
输出一个数表示满足条件的数组的个数。
样例输入
9 1 1 3
样例输出
19683
9 2 1 3
9841
"""
import sys


def solve():
    n, k, L, R = map(int, sys.stdin.readline().strip().split())
    dp = {}
    f = lambda x, i: x // k + len([e for e in range((x // k) * k, x + 1) if e % k == i])
    for i in range(k):
        dp[i] = f(R, i) - f(L - 1, i)
    rec = dp.copy()
    for i in range(1, n):
        tmp = {}
        for x in dp:
            for j in range(k):
                tmp[(x + j) % k] = tmp.get((x + j) % k, 0) + dp[x] * rec[j]
        dp = tmp
    return dp[0]


if __name__ == '__main__':
    res = solve()
    print(res)
