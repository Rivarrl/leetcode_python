# -*- coding: utf-8 -*-
# ======================================
# @File    : t1.py
# @Time    : 2020/3/14 19:33
# @Author  : Rivarrl
# ======================================
import sys

"""
t1 买饮料，饮料买一送一，问最少需要买多少饮料能满足所有人需要
输入：n人数，m饮料种类，n个人的选择
输出：购买数量
输入：
5 3
1 2 1 2 3
输出：
3
"""

def solve():
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    arr = list(map(int, sys.stdin.readline().strip().split(' ')))
    d = {}
    for e in arr:
        d[e] = d.get(e, 0) + 1
    res = 0
    for k, v in d.items():
        res += (v // 2 + v % 2)
    return res

if __name__ == '__main__':
    res = solve()
    print(res)