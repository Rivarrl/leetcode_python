# -*- coding: utf-8 -*-
# ======================================
# @File    : t2.py
# @Time    : 2020/3/12 22:25
# @Author  : Rivarrl
# ======================================
"""
2. 最好一样
给出一个序列包含n个正整数的序列A，然后给出一个正整数x，你可以对序列进行任意次操作的，每
次操作你可以选择序列中的一个数字，让其与x做异或运算。你的目的是让这个序列中的众数出现的次数
最多。
请问众数最多出现多少次。
n x
5 2
3 1 3 2 5
样例输出
3
样例解释
例如如果序列中所有数字都不修改时，众数为3，3出现的次数为2，如果我们把两个3都做如题操作，序列
会变为1，1，1，2，5，
此时众数为1，出现次数为3，所以我们选择后者方案，输出众数出现的次数，即3。
"""
import sys


def solve():
    n, x = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    d = {}
    for e in arr:
        d[e] = d.get(e, 0) + 1
        d[e ^ x] = d.get(e ^ x, 0) + 1
    return max(d.values())


if __name__ == '__main__':
    res = solve()
    print(res)
